# encoding=utf8
from demo.celery import app
from delivery.models import Delivery
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse,redirect, reverse
from subprocess import Popen, PIPE
import shutil, sh, os, re


@app.task
def deploy(ids):
    '''
    部署任务
    :param ids: 交付列表id
    :return:
    '''

    deli = Delivery.objects.filter(id=ids).first()
    project_name = deli.job_name.name
    deploy_num = deli.deploy_num
    workspace = '/var/opt/demo/workspace/{}/'.format(project_name)
    log_name = 'deploy_'+str(deploy_num)+'.log'
    log_path = workspace + 'logs/' + log_name
    code_path = workspace + 'code/'
    s_path = workspace + 'scripts/'
    server_list = deli.job_name.serverList.all()
    source_addr = deli.job_name.source_address

    with open(log_path, 'wb') as f:
        f.writelines("<h4>******STEP: Deploying Project {0} For {1} Th******</h4>\n".format(project_name, deploy_num))

    app_path = deli.job_name.appPath
    if not app_path.endswith('/'):
        app_path += '/'

    deli.bar_data = 20
    deli.save()

    if deli.build_clean or deli.version:
        try:
            with open(log_path, 'ab+') as f:
                f.writelines("<h4>******STEP: CLEAN CODE******</h4>\n")
            shutil.rmtree(code_path)
        except:
            f.writelines('clean over\n')

    with open(log_path + log_name, 'ab+') as f:
        f.writelines("<h4>******STEP: GIT SOURCE CODE******</h4>\n")
    if deli.auth:
        auth_info = {"username": deli.auth.username, "password": deli.auth.password}
    else:
        auth_info = None
    if deli.job_name.source_type == 'git':
        cmd = git_clone(workspace, auth_info, source_addr, deli)
    elif deli.job_name.source_type == 'svn':
        cmd = svn_clone(workspace, auth_info, source_addr, deli)
    else:
        with open(log_path, 'ab+') as f:
            f.writelines("source_type error")
        return HttpResponse("source_type error")
    data = exec_cmd(cmd)
    with open(log_path, 'ab+') as f:
        f.writelines(cmd),
        f.writelines('\n'),
        f.writelines(data),
    deli.bar_data = 30
    deli.save()

    if deli.shell:
        with open(log_path, 'ab+') as f:
            f.writelines("<h4>******STEP: DEPLOY SHELL EXECUTE******</h4>\n")
        shell_path = s_path + 'deploy_'+str(deploy_num)+'.sh'
        with open(shell_path, 'ab+') as f:
            f.writelines(deli.shell)
        cmd = '/usr/bin/dos2unix {}'.format(shell_path)
        data = exec_cmd(cmd)
        with open(log_path, 'ab+') as f:
            f.writelines(data)

    r_code = "--delete" if deli.rsync_del else "--code"
    # if deli.rsync_del:
    #     r_code = "--delete"
    # else:
    #     r_code = "--code"

    exclude_file = code_path + 'exclude.txt'
    for server in server_list:
        _ip = str(server.ip)
        sh.ssh("root@{}".format(_ip), "mkdir -p {}".format(app_path))

        with open(log_path, 'ab+') as f:
            f.writelines("<h4>******STEP: RSYNC THE CODE TO {}******</h4>\n".format(app_path))
        if os.path.exists(exclude_file):
            cmd = "rsync --progress -raz {4} --exclude-from {3} {0} {1}:{2}".format(
                code_path, _ip, app_path, exclude_file, r_code)
        else:
            cmd = "rsync --progress -raz {3} --exclude '.git' --exclude '.svn' {0} {1}:{2}".format(
                code_path, _ip, app_path, r_code)
        data = exec_cmd(cmd)
        with open(log_path, 'ab+') as f:
            f.writelines(data)

        if deli.shell and not deli.shell_position:  # 远程执行shell脚本
            with open(log_path, 'ab+') as f:
                f.writelines("<h4>******STEP: EXECUTE SHELL REMOTE******</h4>\n")
            cmd = "scp {0} root@{1} /tmp/".format(shell_path, _ip)
            data = exec_cmd(cmd)
            with open(log_path, 'ab+') as f:
                f.writelines(data)
            cmd = 'sh /tmp/deploy_'+str(deploy_num)+'.sh'
            data = exec_cmd(cmd)
            with open(log_path, 'ab+') as f:
                f.writelines(data)

        if deli.bar_data < 94:
            deli.bar_data += 5
            deli.save()

        if deli.shell and deli.position:
            with open(log_path, 'ab+') as f:
                f.writelines("<h4>******STEP: EXECUTE SHELL POSITION******</h4>\n")
            data = sh.bash(shell_path)
            with open(log_path, "ab+") as f:
                f.writelines(data)

    deli.bar_data = 100
    deli.status = False
    deli.save()

    with open(log_path, "ab+") as f:
        f.writelines("<h4>******STEP: Project {0} Have Deployed For {1}Th******</h4>\n".format(project_name, deploy_num))

    return data


def exec_cmd(cmd):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    return p.communicate()


def parser_url(source_address, url_len, user_len, auth_info, url_type=None):
    if url_type:
        new_suffix = source_address[url_len:][user_len:]
        final_add = source_address[:url_len] + auth_info["username"] + ":" + auth_info["password"] + new_suffix
    else:
        new_suffix = source_address[url_len:]
        final_add = source_address[:url_len] + auth_info["username"] + ":" + auth_info["password"] + new_suffix
    return final_add


def git_clone(job_workspace, auth_info, source_address, p1):
    if os.path.exists("{0}code/.git".format(job_workspace)):
        cmd = "cd {0}code/ && git pull".format(job_workspace)
        return cmd
    if auth_info and p1.job_name.source_address.startswith("http"):
        url_type = re.search(r'(@)', source_address)
        if url_type:
            user_len = len(auth_info["username"])
            if source_address.startswith("https://"):
                url_len = 8
            else:
                url_len = 7
            source_address = parser_url(source_address, url_len, user_len, auth_info, url_type)
        else:
            if source_address.startswith("https://"):
                url_len = 8
            else:
                url_len = 7
            source_address = parser_url(source_address, url_len, auth_info, url_type)
    if p1.version:
        cmd = "git clone -b {2} {0} {1}code/".format(source_address, job_workspace, p1.version)
    else:
        cmd = "git clone {0} {1}code/".format(source_address, job_workspace)
    return cmd


def svn_clone(job_workspace, auth_info, source_address, p1):
    if p1.version:
        if not source_address.endswith("/") and not p1.version.endswith('/'):
            source_address += '/'
        source_address += p1.version
    if os.path.exists("{0}code/.svn".format(job_workspace)):
        cmd = "svn --non-interactive --trust-server-cert --username {2} --password {3} update {0} {1}code/".format(
                source_address, job_workspace, auth_info["username"], auth_info["password"])
    else:
        cmd = "svn --non-interactive --trust-server-cert --username {2} --password {3} checkout {0} {1}code/".format(
                source_address, job_workspace, auth_info["username"], auth_info["password"])
    return cmd