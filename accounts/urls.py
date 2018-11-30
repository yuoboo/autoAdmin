from django.conf.urls import url
import views

urlpatterns = [
    # url(r'$', views.index, name='index'),
    url(r'login/$', views.login, name='login'),
    url(r'logout/$', views.logout, name='logout'),

    url(r'change/password/$', views.password_change, name='password_change'),

    url(r'user/add/$', views.user_add, name='user_add'),
    url(r'user/list/$', views.user_list, name='user_list'),
    url(r'user/edit/(?P<ids>\d+)/$', views.user_edit, name='user_edit'),
]
