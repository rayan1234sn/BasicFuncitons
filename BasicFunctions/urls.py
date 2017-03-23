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
from django.conf.urls import include, url 
from django.contrib import admin
from candidateManager.views import * 
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    url(r'^login/$', auth_views.login, {'template_name': 'candidateManager/login.html'} ,name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'},  name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^locations/', include('candidateManager.location_urls')),
    url(r'^candidates/', include('candidateManager.candidate_urls')),
    url(r'^jobrequesitons/', include('candidateManager.jobrequesition_urls')),
    url(r'^$', Home.as_view()),

]