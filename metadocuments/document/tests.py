import json

from rest_framework.test import APITestCase

from .models import Document


class DocumentTestCase(APITestCase):

    def test01(self):
        document_data = {'document_number': '112233',
                         'document_date': '2014-05-01',
                         'amount': '100.00',
                         'currency': 'EUR'}
        resp  = self.client.post('/document',
                                 json.dumps(document_data),
                                 content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data.get('document_number'), '112233')
        docs = Document.objects.all()
        self.assertEqual(len(docs), 1)

