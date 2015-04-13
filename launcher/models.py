from django.db import models

class Application(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    description = models.TextField(blank=True)
    command = models.CharField(max_length=256)
    icon = models.FileField(upload_to='icons', blank=True)
    notes = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.pk
