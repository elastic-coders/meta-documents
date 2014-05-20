from django.db import models

from meta import make_document_app


'''
config = {'model':
              {'fields': [
                  {'name': 'receipt_date',
                   'type': models.DateField(blank=True, null=True)},
                  {'amount': 'receipt_date',
                   'type': models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)},
                  {'name': 'currency',
                   'type': models.CharField(max_length=3, blank=True, null=True)},
              ]},
          'views': [{'type': 'list'},
                    {'type': 'detail'},]}
'''

config = {'model':
              {'concrete':
                  {'name': 'meta_receipt',
                   'from': 'meta_receipt.models'},
              },
          'views': [{'type': 'list'},
                    {'type': 'detail'},]}

application = make_document_app('meta_receipt', config)