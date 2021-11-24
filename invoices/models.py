from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from Util.utils import rand_slug
#  Invoice class is responsible for modeling Invoice attributes and functions
class Invoice(models.Model):
    # invoice number
    number = models.CharField(
        max_length=300,
        blank=False,
        null=False,
        unique=True
    )
    # invoice QR code
    qr_code = models.CharField(
        max_length=450,
        blank=False,
        null=False,
        unique=True
    )
    # invoice due date
    due_date = models.DateField(
        blank=False,
        null=False
    )
    # invoice payment status
    payment_status = models.CharField(
        max_length=230,
        blank=False,
        null=False
    )
    # invoice sender email , foreign key refers
    # to accounts user (sender)
    sender_email = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name="sender_email"
    )
    # invoice receiver email , foreign key refers
    # to accounts user (receiver)
    receiver_email = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name="receiver_email"
    )
    # invoice slug field
    slug = models.SlugField(
        default=slugify(rand_slug()),
        verbose_name=_('Invoice Slug')
    )

class InvoiceItem(models.Model):
    # foreign key refers to Invoice table
    invoice_id = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )
    # item field, bought by the customer
    item = models.CharField(
        max_length=400,
        blank=False,
        null=True
    )
    # unit price of an item
    unit_price = models.FloatField(
        blank=False,
        null=False
    )
    # quantity field
    quantity = models.IntegerField(
        blank=False,
        null=False
    )