from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^register/$', register),
    url(r'^register_handler/$', register_handler),
    url(r'^check_name/$', check_name),
    url(r'^login/$', login),
    url(r'^login_handler/$', login_handler),
]

