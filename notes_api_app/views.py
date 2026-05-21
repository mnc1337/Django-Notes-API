"""
App views
"""

from django.shortcuts import render


def home_app(request):
    return render(request, "notes_api_app/home.html", {}, using="jinja2")
