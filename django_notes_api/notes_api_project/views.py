"""
Project views
"""

from django.shortcuts import render, redirect
from notes_api_app.forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages


def home_project(request):
    return render(request, "home.html", {}, using="jinja2")


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST, prefix="user")
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("create_user")

    else:
        form = UserForm(prefix="user")

    return render(request, "create_user.html", {"form": form}, using="jinja2")


class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        messages.success(
            self.request, "You have successfully logged in to your account!"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Incorrect username or password. Try again.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = messages.get_messages(self.request)
        return context
