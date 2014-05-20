from django.db import models

from meta import make_document_app


config = {'model':
              {'concrete':
                  {'name': 'meta_bill',
                   'from': 'meta_bill.models'},
              },
          'views': [{'type': 'list'},
                    {'type': 'detail'},]}

application = make_document_app('meta_bill', config)