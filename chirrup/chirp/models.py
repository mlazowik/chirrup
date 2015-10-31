from django.conf import settings
from django.db import models


class Chirp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.CharField(max_length=settings.MAX_CHIRP_LENGTH)
    added = models.DateTimeField()

    class Meta:
        ordering = ['-added']

    def get_content(self):
        return self.text

    def __unicode__(self):
        return self.get_content()