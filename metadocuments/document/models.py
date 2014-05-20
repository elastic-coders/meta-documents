from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    ''' standard implementation of a simple document

    '''

    document_number = models.CharField(max_length=10, null=True, blank=True)
    document_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)

