from django.contrib import admin
from .models import Invoice,InvoiceItem
# Register Invoice and InvoiceItem data models to admin dashboard
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
