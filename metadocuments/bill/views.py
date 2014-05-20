from django.shortcuts import render

from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Bill
from .serializers import BillSerializer


class BillListView(ListCreateAPIView):
    ''' this is a simple view implemented
        inheriting view from ListCreateAPIView
        For easy code we not authenticate the view
    '''
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer