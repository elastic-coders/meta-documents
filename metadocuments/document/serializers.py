from __future__ import absolute_import

from rest_framework import serializers

from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        read_only_fields = ['id']

