from rest_framework import permissions, viewsets

from .models import Prompt
from .serializers import PromptSerializer


class PromptViewSet(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prompt.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)