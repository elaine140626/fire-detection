"""fire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from login import views
from login import user, messages, device, video

user_patterns = [
    path('login/', user.login_controller),
    path('check_login/', user.check_is_login_and_get_username_controller)
]
message_patterns = [
    path('', messages.messages),
    path('info/', messages.get_message_info_controller),
    path('approve', messages.approve_message_controller),
]

device_patterns = [
    path('', device.device_controller),
    path('all/', device.get_all_device_controller)
]

video_patterns = [
    path('', video.videos_controller)
]

api_patterns = [
    path('user/', include(user_patterns)),
    path('messages/', include(message_patterns)),
    path('devices/', include(device_patterns)),
    path('videos/', include(video_patterns)),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', views.MessageAmount),
    path('warning/true/', views.dealTrue),
    path('warning/false/', views.dealFalse),
    path('warning/', views.warning),
    path('login/', views.login),
    path('monitor/', views.monitor),
    path('overview/', views.overview),
    path('logout/', views.logout),
    path('data', views.DealData),
    path('conf/', views.conf),
    path('wechat', views.wechat),
    path('user_config', views.getUserConf),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/', include(api_patterns))
]
