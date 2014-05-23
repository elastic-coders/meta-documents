import json

from rest_framework.test import APITestCase


class AllTestCase(APITestCase):

    def test01(self):
        document_data = {'bill_number': '112233',
                         'bill_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR',
                         'provider': 'Enel'}
        resp  = self.client.post('/billapp',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.get('bill_number'), '112233')
        id = resp.data.get('id')
        resp  = self.client.get('/billapp/{}'.format(id),)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('bill_number'), '112233')
        self.assertEqual(resp.data.get('provider'), 'Enel')


    def test02(self):
        document_data = {'document_number': '112233',
                         'document_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR'}
        resp  = self.client.post('/documentapp',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.get('document_number'), '112233')
        id = resp.data.get('id')
        resp  = self.client.get('/documentapp/{}'.format(id),)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('document_number'), '112233')

    def test03(self):
        document_data = {'receipt_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR'}
        resp  = self.client.post('/receiptapp',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        id = resp.data.get('id')
        resp  = self.client.get('/receiptapp/{}'.format(id),)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.get('amount'), 100)

