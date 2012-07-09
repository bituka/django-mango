from django.db import models
from django.core import exceptions
from django.utils.translation import ugettext_lazy as _


class Conference(models.Model):
    name = models.CharField(max_length=100)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    description = models.TextField()
    is_enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def clean(self):
        enabled_conf_count = Conference.objects.filter(is_enabled=True).count()
        if self.is_enabled and enabled_conf_count > 0:
            raise exceptions.ValidationError(
                _(u"There can only be one conference enabled at a time."))
