from cms.models import CMSPlugin
from django.db import models


class IframePlugin(CMSPlugin):
    src = models.URLField(max_length=1000)
