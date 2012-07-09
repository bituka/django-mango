from django.db import models


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
