"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include

from django.contrib import admin
from Mobile_store.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^get_brands/$',get_brands),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^add_brand/$',add_brand),
    url(r'^add_mobiles/$',add_mobiles),
    url(r'^get_mobiles/$',get_mobiles),
    url(r'^view_mobiles/$',view_mobiles),
    url(r'^update_mobiles/(?P<id>[0-9]+)/$',update_mobiles),
    url(r'^delete_mobiles/(?P<id>[0-9]+)/$',delete_mobiles)


]
