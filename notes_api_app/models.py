"""
Models configuration
"""

from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Note(models.Model):
    uuid = models.UUIDField(
        default=uuid4, verbose_name="Note UUID", editable=False, blank=True
    )
    title = models.CharField(max_length=200, verbose_name="Note title")
    content = models.TextField(verbose_name="Note text", null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Note created at", editable=False
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Note updated at", editable=False
    )
    is_important = models.BooleanField(
        default=False, verbose_name="Note is important", blank=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes", blank=True
    )

    def __str__(self):
        return f"Note <{self.uuid}> with title '{self.title}'"

    class Meta:
        ordering = ["-created_at"]
