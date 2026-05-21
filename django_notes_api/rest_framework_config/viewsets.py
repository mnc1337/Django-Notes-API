from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteModelSerializer
from notes_api_app.models import Note


class NoteModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteModelSerializer

    queryset = Note.objects.all()

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
