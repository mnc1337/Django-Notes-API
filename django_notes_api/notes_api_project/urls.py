"""
Project URLs
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_config.routers import router
from graphene_django.views import GraphQLView
from graphql_config.schemas import schema
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "login/",
        views.CustomLoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger_ui",
    ),
    path("graphql/", GraphQLView.as_view(schema=schema, graphiql=True)),
    path("app/", include("notes_api_app.urls")),
    path("", views.home_project, name="home_project"),
    path("create_user/", views.create_user, name="create_user"),
]
