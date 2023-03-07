from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from custom_user.forms import RegistrationForm
from . import models


class Registration(CreateView):
    form_class = RegistrationForm
    success_url = '/books/'
    template_name = 'registration_form.html'


class NewLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse("users:user_list")


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = "user_list.html"

    def get_queryset(self):
        return User.objects.all()