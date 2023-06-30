from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Application(BaseModel):
    title = models.CharField(_("Title"), max_length=256)
    course_name = models.CharField(_("Course Name"), max_length=256)
    study_type = models.CharField(_("Study Type"), max_length=256)
    course_year = models.CharField(_("Course Year"), max_length=256)
    course_language = models.CharField(_("Course Language"), max_length=256)
    # FK
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")


class ApplicationDocument(BaseModel):
    title = models.CharField(_("Title"), max_length=256)
    file = models.FileField(upload_to="applications/%Y/%m/%d")
    # FK
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="documents")

    class Meta:
        verbose_name = _("ApplicationDocument")
        verbose_name_plural = _("ApplicationDocuments")
