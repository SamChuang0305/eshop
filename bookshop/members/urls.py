from django.conf.urls import url
from members import views as views

urlpatterns = [
    url(r'^profile/(?P<pk>\d+)/$', views.member_profile_view, name='member_profile')
]