from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^register/$', register),
    url(r'^register_handler/$', register_handler),
    url(r'^check_name/$', check_name),
    url(r'^login/$', login),
    url(r'^checkloginstatus/$', check_login_status),
    url(r'^index/$', login_handler),
    url(r'^loginstatus/$', login_status),
    url(r'^quitlogin/$', quit_login),
]

