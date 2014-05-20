import json

from rest_framework.test import APITestCase

from .models import Bill


class BillTestCase(APITestCase):

    def test01(self):
        document_data = {'bill_number': '112233',
                         'bill_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR',
                         'provider': 'Enel'}
        resp  = self.client.post('/bill',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.get('bill_number'), '112233')
        self.assertEqual(resp.data.get('provider'), 'Enel')
        docs = Bill.objects.all()
        self.assertEqual(len(docs), 1)

    def test02(self):
        document_data = {'bill_number': '112233',
                         'bill_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR',
                         'provider': 'Enel'}
        resp  = self.client.post('/bill',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.get('bill_number'), '112233')
        id = resp.data.get('id')
        resp  = self.client.get('/bill/{}'.format(id),)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('bill_number'), '112233')
        self.assertEqual(resp.data.get('provider'), 'Enel')

