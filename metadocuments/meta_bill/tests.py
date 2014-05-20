import json

from rest_framework.test import APITestCase

from .models import meta_bill


class MetaReceiptTestCase(APITestCase):

    def test01(self):
        document_data = {'bill_number': '38197',
                         'bill_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR',
                         'provider': 'Enel',
                         'energy': '121'}
        resp  = self.client.post('/meta_bill',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.get('amount'), 100)
        self.assertEqual(resp.data.get('provider'), 'Enel')
        self.assertEqual(resp.data.get('energy'), 121)
        docs = meta_bill.objects.all()
        self.assertEqual(len(docs), 1)

    def test02(self):
        document_data = {'bill_number': '38197',
                         'bill_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR',
                         'provider': 'Enel',
                         'energy': '121'}
        resp  = self.client.post('/meta_bill',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        id = resp.data.get('id')
        resp  = self.client.get('/meta_bill/{}'.format(id),)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('amount'), 100)
        self.assertEqual(resp.data.get('provider'), 'Enel')
        self.assertEqual(resp.data.get('energy'), 121)

