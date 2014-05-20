from __future__ import absolute_import

from rest_framework import serializers

from .models import Bill


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        read_only_fields = ['id']

