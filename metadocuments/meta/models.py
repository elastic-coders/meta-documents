from django.db import models

# Create your models here.

class MetaModel(models.Model):

    class Meta:
        abstract = True