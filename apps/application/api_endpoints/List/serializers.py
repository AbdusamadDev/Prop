from rest_framework import serializers

from apps.application.models import Application, ApplicationDocument
from apps.users.models import User


class ApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocument
        fields = ("title", "file")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "full_name", "phone", "faculty", "course")


class ApplicationListSerializer(serializers.ModelSerializer):
    documents = ApplicationDocumentSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Application
        fields = (
            "id",
            "title",
            "user",
            "course_name",
            "study_type",
            "course_year",
            "course_language",
            "documents",
        )
