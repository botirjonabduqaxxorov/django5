# from django.db import models

from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
