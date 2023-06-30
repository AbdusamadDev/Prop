from rest_framework import generics
from apps.application.api_endpoints.Create.serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from apps.application.models import Application


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = ['ApplicationCreateView']
