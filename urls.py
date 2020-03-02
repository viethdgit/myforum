"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from . import views

urlpatterns = [
    url('forum/login.html', views.login, name='login'),
    url('forum/sign_up.html', views.sign_up, name='sign_up'),
    url('forum/main_page.html', views.main_page, name='main_page'),
    url('forum/new_thread.html', views.new_thread, name='new_thread'),
    url('forum/logout.html', views.logout, name='logout'),
    url('forum/thread_id=(?P<tid>[0-9]+)$',views.thread_id),

    url('forum/chatbox.html',views.chatbox),
    url('forum/chat_content.html',views.chat_content),
]
