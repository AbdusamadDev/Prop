from rest_framework import serializers

from apps.application.models import Application


# class ApplicationDocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApplicationDocument
#         fields = ("title", "file")


class ApplicationSerializer(serializers.ModelSerializer):
    # documents = ApplicationDocumentSerializer(many=True)

    class Meta:
        model = Application
        fields = '__all__'

    # def create(self, validated_data):
    #     documents = validated_data.pop("documents")
    #     application = Application.objects.create(**validated_data)
    #
    #     for document in documents:
    #         ApplicationDocument.objects.create(application=application, **document)
    #     return application
