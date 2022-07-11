"""restapi_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from practice import views

#import practice.api

#app_name = 'practice'

router = routers.DefaultRouter()
#router.register('practices', views.PracticeViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('practices/', views.practice_list),
    path('practice/<int:id>/', views.practice),
    path('login/', views.login),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
