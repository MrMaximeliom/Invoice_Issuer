from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


# this class is responsible to make the serialization processing for Invoice data model
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        from invoices.models import Invoice
        # choosing "Invoice Model" to serialize its objects
        model = Invoice
        # all fields of the Invoice model - except of "slug" field - will be available in the API endpoint later
        exclude = ('slug',)


# this class is responsible to make the serialization processing for Invoice data model
class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        from invoices.models import InvoiceItem
        # choosing "InvoiceItem Model" to serialize its objects
        model = InvoiceItem
        # all fields of the InvoiceItem model - except of "slug" field - will be available in the API endpoint later
        exclude = ('slug',)
