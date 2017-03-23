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
    
    url(r'^$', Candidates_List.as_view(), name='candidate_list'),
    url(r'^new$', Candidates_Create.as_view(), name='candidate_new'),
    url(r'^edit/(?P<pk>\d+)$', Candidates_Update.as_view(), name='candidate_edit'),
    url(r'^delete/(?P<pk>\d+)$', Candidates_Delete.as_view(), name='candidate_delete'),
    url(r'^detail/(?P<pk>\d+)$', Candidates_Detail.as_view(), name='candidate_detail'),
    url(r'^notes/add/(?P<pk>\d+)$', Note_Create.as_view(), name='notes_create'),
]
