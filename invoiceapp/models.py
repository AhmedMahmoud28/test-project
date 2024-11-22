from django.db import models

# Create your models here.


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey("invoiceapp.Invoice", on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    line_total = models.DecimalField(max_digits=5, decimal_places=2)
