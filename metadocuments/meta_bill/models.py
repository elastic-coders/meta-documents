from __future__ import absolute_import

from django.db import models

class meta_bill(models.Model):
    bill_number = models.CharField(max_length=10, null=True, blank=True)
    bill_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    provider = models.CharField(max_length=40, blank=True, null=True)
    energy = models.IntegerField(blank=True, null=True)

'''
from . import application


model = application['model']
globals()[model.__name__] = model
del model
'''