from cms.models import CMSPlugin
from django.db import models


class IframePlugin(CMSPlugin):
    src = models.URLField(max_length=1000)
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
