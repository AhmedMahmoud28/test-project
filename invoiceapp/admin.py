from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from . import models


class InvoiceDetailInline(StackedInline):
    model = models.InvoiceDetail
    min_num = 0
    extra = 0


@admin.register(models.Invoice)
class BranchAdmin(ModelAdmin):
    list_display = ("id", "invoice_number", "customer_name", "date")
    search_fields = ("invoice_number", "customer_name")
    inlines = [InvoiceDetailInline]
