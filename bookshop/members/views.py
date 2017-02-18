from django.views.generic import DetailView, CreateView, TemplateView
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from members.forms import RegistrationForm


class MemberProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'members/profile.html'


class RegistrationView(LoginRequiredMixin, CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'members/registration.html'

    def get_success_url(self):
        return reverse('success')


class SuccessMessageView(LoginRequiredMixin, TemplateView):
    template_name = 'members/registration_success.html'


member_profile_view = MemberProfileView.as_view()
member_registration_view = RegistrationView.as_view()
success_message_view = SuccessMessageView.as_view()
