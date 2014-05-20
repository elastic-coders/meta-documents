from django.shortcuts import render

from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Receipt
from .serializers import ReceiptSerializer


class ReceiptListView(ListCreateAPIView):
    ''' this is a simple view implemented
        inheriting view from ListCreateAPIView
        For easy code we not authenticate the view
    '''
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class ReceiptDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer