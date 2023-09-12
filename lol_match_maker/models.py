from django.db import models

# Create your models here.


class Champion(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    type = models.CharField(max_length=120)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
