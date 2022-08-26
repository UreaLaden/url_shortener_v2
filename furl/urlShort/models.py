from django.db import models

# Create your models here.
class urlModel(models.Model):
    original_url = models.CharField(max_length=255)
    short_url  = models.CharField(max_length=7)
    count  = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.short_url