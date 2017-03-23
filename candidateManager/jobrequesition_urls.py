"""BasicFunctions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from candidateManager.views import * 


urlpatterns = [
    
    url(r'^$', JobRequesition_List.as_view(), name='jobRequesition_list'),
    url(r'^new$', JobRequesition_Create.as_view(), name='jobRequesition_new'),
    url(r'^edit/(?P<pk>\d+)$', JobRequesition_Update.as_view(), name='jobRequesition_edit'),
    url(r'^delete/(?P<pk>\d+)$', JobRequesition_Delete.as_view(), name='jobRequesition_delete'),
    url(r'^detail/(?P<pk>\d+)$', JobRequesition_Detail.as_view(), name='jobRequesition_detail'),
    url(r'^candidates/(?P<pk>\d+)$', JobRequesition_FilterList.as_view(), name='jobRequesition_filter'),
]
