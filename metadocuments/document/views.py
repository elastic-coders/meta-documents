from django.shortcuts import render

from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Document
from .serializers import DocumentSerializer


class DocumentListView(ListCreateAPIView):
    ''' this is a simple view implemented
        inheriting view from ListCreateAPIView
        For easy code we not authenticate the view
    '''
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer