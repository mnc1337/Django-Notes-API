from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from notes_api_app.models import Note


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "email", "is_superuser", "notes")


class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        fields = ("id", "uuid", "title", "content", "created_at", "is_important")
