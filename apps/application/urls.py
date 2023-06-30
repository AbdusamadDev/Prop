from django.urls import path
from apps.application.api_endpoints.Create import ApplicationCreateView

urlpatterns = [
    path('', ApplicationCreateView.as_view(), name='application-create'),
]