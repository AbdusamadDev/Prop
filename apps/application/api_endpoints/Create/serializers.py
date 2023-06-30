from rest_framework import serializers

from apps.application.models import Application, ApplicationDocument


class ApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocument
        fields = ("title", "file")


class ApplicationSerializer(serializers.ModelSerializer):
    documents = ApplicationDocumentSerializer(many=True)

    class Meta:
        model = Application
        fields = (
            "title",
            "course_name",
            "study_type",
            "course_year",
            "course_language",
            "documents",
        )

    def create(self, validated_data):
        documents = validated_data.pop("documents")
        application = Application.objects.create(**validated_data)

        for document in documents:
            ApplicationDocument.objects.create(application=application, **document)
        return application
