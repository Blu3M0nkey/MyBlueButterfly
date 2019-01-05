from django.conf.urls import url
import django.contrib.auth.views
from datetime import datetime


from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),

    

]