from django.views.generic import DetailView
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class MemberProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'members/profile.html'


member_profile_view = MemberProfileView.as_view()
