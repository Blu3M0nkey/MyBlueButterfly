"""
Definition of urls for MyBlueButterfly.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin

import Main.forms
import Main.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include

urlpatterns = [
    # Examples:
    url(r'^', include('Main.urls')),
   
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'login.html',
            'authentication_form': Main.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
