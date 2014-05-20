import json

from rest_framework.test import APITestCase

from .models import meta_receipt


class MetaReceiptTestCase(APITestCase):

    def test01(self):
        document_data = {'receipt_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR',
                         'provider': 'Vodafone'}
        import pdb; pdb.set_trace()
        resp  = self.client.post('/meta_receipt',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.get('amount'), 100)
        self.assertEqual(resp.data.get('provider'), 'Vodafone')
        docs = meta_receipt.objects.all()
        self.assertEqual(len(docs), 1)

    def test02(self):
        document_data = {'receipt_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR'}
        resp  = self.client.post('/meta_receipt',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        id = resp.data.get('id')
        resp  = self.client.get('/meta_receipt/{}'.format(id),)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('amount'), 100)

