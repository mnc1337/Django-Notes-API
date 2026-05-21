from rest_framework import routers
from .viewsets import NoteModelViewSet

router = routers.SimpleRouter()
router.register(r"notes", NoteModelViewSet, basename="note")

router_urlpatterns = router.urls
