from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from django.utils.translation import gettext as _

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin
from django.contrib.messages.views import SuccessMessageMixin

from project.forms import SignUpForm, ProfileSettingsForm, LoginForm
from project.models import Profile


# django-admin makemessages -l ru
# python manage.py compilemessages --use-fuzzy
    

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    extra_context = {
    }


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    next_page = 'index'
    # TODO Correctly check if the fields are correct
    # TODO Fix authorization


class ProfileSettingsView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile_edit.html'
    model = User
    form_class = ProfileSettingsForm
    success_url = reverse_lazy('index')
    context_object_name = 'user'

    def get_object(self, queryset=None):
        user = self.request.user
        profile = user.profile
        self.initial['nickname'] = profile.nickname
        self.initial['avatar'] = profile.avatar
        return user


class ProfileView(DetailView):
    template_name = 'registration/profile.html'
    model = Profile
    context_object_name = 'profile'
    extra_context = {
    }

