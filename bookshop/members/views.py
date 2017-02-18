from django.views.generic import DetailView, CreateView, TemplateView
from django.urls import reverse
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from members.forms import RegistrationForm


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'members/profile.html'

    def get_object(self, *args, **kwargs):
        current_user = self.request.user
        user = super(ProfileView, self).get_object(*args, **kwargs)

        if current_user.is_superuser or current_user.is_staff or current_user == user:
            return user

        raise PermissionDenied


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'members/registration.html'

    def get_success_url(self):
        return reverse('success')


class SuccessMessageView(TemplateView):
    template_name = 'members/registration_success.html'


member_profile_view = ProfileView.as_view()
member_registration_view = RegistrationView.as_view()
success_message_view = SuccessMessageView.as_view()
