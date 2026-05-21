"""
Admin panel configuration
"""

from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteModelAdmin(admin.ModelAdmin):
    list_display = ["title", "uuid", "created_at", "user"]
    sortable_by = ["title", "uuid", "created_at", "user"]
    list_filter = ["title", "uuid", "user"]
