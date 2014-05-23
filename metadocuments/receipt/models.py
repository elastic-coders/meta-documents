from django.db import models


class Receipt(models.Model):
    ''' standard implementation of a simple document call receipt

    '''

    receipt_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)

