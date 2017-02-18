from django.conf.urls import url
from members import views as views

urlpatterns = [
    url(r'^profile/(?P<pk>\d+)/$', views.member_profile_view, name='member_profile'),
    url(r'^registration/$', views.member_registration_view, name='registration'),
    url(r'^registration/success/$', views.success_message_view, name="success")
]
