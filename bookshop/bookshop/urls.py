"""bookshop URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from books import views
from members.forms import LoginForm

urlpatterns = [
    url(r'^$', views.book_list_view, name='home'),
    url(r'^books/(?P<category>.*)/$', views.book_list_view, name='book_list'),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail_view, name='book_detail'),
    url(r'^login/$', auth_views.login, {'template_name': 'members/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^socialauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
