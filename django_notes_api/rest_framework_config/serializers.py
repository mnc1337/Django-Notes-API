from rest_framework import serializers
from notes_api_app.models import Note


class NoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            "id",
            "uuid",
            "title",
            "content",
            "created_at",
            "updated_at",
            "is_important",
            "user",
        )
        read_only_fields = ("uuid", "created_at", "user")
