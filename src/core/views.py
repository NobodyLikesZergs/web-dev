from django.shortcuts import resolve_url
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'core/create_user.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('core:login')


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'core/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('questions:question_list')
