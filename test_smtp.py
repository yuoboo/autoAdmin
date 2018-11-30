# encoding=utf-8
import smtplib
import string
from email.mime.text import MIMEText   # 支持plain(默认)或者 html类型的字符串
from email.mime.audio import MIMEAudio  # 发送音频
from email.mime.image import MIMEImage  # 发送图片
from email.mime.multipart import MIMEMultipart   # 混合
import socket

HOST = "smtp.163.com"   # 测试主机
SUBJECT = "Test email from server"    # 邮件主题
TO = "yuoboo1008@foxmail.com"    # 邮件接受方
FROM = "yuoboo1008@163.com"     # 邮件发送方
PASSWORD = 'yubing107217'
COUNT = 1   # 计数


class SendEmail(object):
    
    def __init__(self):
        self._host = HOST
        self._from = FROM
        self._to = TO
        self._password = PASSWORD
        self._subject = SUBJECT
        self._hostname, self._ipaddr = self.get_ip()

    def get_ip(self):
        try:
            hostname = socket.getfqdn(socket.gethostname())
            ipaddr = socket.gethostbyname(hostname)
        except Exception as msg:
            print(msg)
            hostname = ''
            ipaddr = ''
        return hostname, ipaddr

    def send(self, _body):
        server = smtplib.SMTP()
        server.connect(self._host, '25')
        server.starttls()  # 开启加密传送
        server.login(self._from, self._password)
        server.sendmail(self._from, [self._to], _body)
        server.quit()

    # 普通文字 email
    def send_email(self):

        Text = "this is email content"    # 邮件内容

        # 组装sendmail邮件主题内容
        BODY = string.join(("From: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, '', Text), '\r\n')

        self.send(BODY)

    # 发送带html email
    def send_mime_text(self):
        '''

        :return:
        '''
        msg = MIMEText("""
        <p><a href="134.175.101.39">运维平台>></a></p>
        <button class="ce-ajax" style="background-color:rgb(165,42,42); height: 50px;width: 150px;">邮件测试button</button>
        <h4>亲, 请记得打下班卡</h4>
        <p>From: server_ip:{0}; server_name:{1}</>
        """.format(self._ipaddr, self._hostname), 'html', 'utf-8')
        msg["Subject"] = self._subject
        msg["From"] = self._from
        msg["To"] = self._to

        self.send(msg.as_string())


if __name__ == '__main__':

    # msg = u'发送第{}次'.format(COUNT)
    SendEmail().send_mime_text()
    print 'this is over'
    # COUNT = COUNT + 1
