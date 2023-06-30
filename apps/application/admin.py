from django.contrib import admin
from apps.application.models import Application, ApplicationDocument


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    list_display_links = ('title',)


@admin.register(ApplicationDocument)
class ApplicationDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
