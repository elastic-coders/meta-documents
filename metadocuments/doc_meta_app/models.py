from django.db import models


class MyBill(models.Model):
    ''' standard implementation of a simple document

    '''

    bill_number = models.CharField(max_length=10, null=True, blank=True)
    bill_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    provider = models.CharField(max_length=40, blank=True, null=True)

class MyDocument(models.Model):
    ''' standard implementation of a simple document

    '''

    document_number = models.CharField(max_length=10, null=True, blank=True)
    document_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)

class MyReceipt(models.Model):
    ''' standard implementation of a simple document call receipt

    '''

    receipt_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)

