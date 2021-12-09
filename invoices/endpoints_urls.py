from django.utils.translation import gettext_lazy as _
from rest_framework import mixins
from rest_framework import viewsets
from Util.permissions import SenderPermission

# this class is used to create new Invoices
class InvoiceViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows to create new invoices
        permissions to this view is restricted as the following:
        - sender users
         only can access this api to create an invoice
         Data will be submitted in the following format using POST function:
       {
        "id": 26,
        "number": "invoice number",
        "qr_code": "qr_code",
        "due_date":"23/3/2012",
        "payment_status":"paid/unpaid",
        "sender_email": "ali@gmail.com",
        "receiver_email": "adel@gmail.com",
        }
      """
    from invoices.serializers import InvoiceSerializer
    # set view Name as "Create/Modify New Invoices"
    def get_view_name(self):
        return _("Create/Modify New Invoices")
    from .models import Invoice
    queryset = Invoice.objects.all()
    # specifying serializar class
    serializer_class = InvoiceSerializer
    # set permission to access this view
    permission_classes = [SenderPermission]


# this class is used to create invoice items
class InvoiceItemViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows to create new invoice items
        permissions to this view is restricted as the following:
        - sender users
         only can access this api to create an invoice
         Data will be submitted in the following format using POST function:
       {
        "id": 26,
        "invoice_id": 11,
        "item": "item name",
        "unit_price":"240 SDG",
        "quantity":"2",
        }
      """
    from invoices.serializers import InvoiceItemSerializer
    # set view Name as "Create/Modify New Invoice Items"
    def get_view_name(self):
        return _("Create/Modify New Invoice Items")
    from .models import InvoiceItem
    # get all Invoices Items from DB
    queryset = InvoiceItem.objects.all()
    # specifying serializer class
    serializer_class = InvoiceItemSerializer
    # set permission to access this view
    permission_classes = [SenderPermission]
