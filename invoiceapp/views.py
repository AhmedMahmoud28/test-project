from rest_framework import viewsets

from . import models, serializers

# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all().prefetch_related("invoicedetail_set")
    serializer_class = serializers.InvoiceSerializer
    http_method_names = ["get", "post", "put"]

    def get_serializer_class(self):
        if self.action in ["create", 'update']:
            return serializers.CreateInvoiceSerializer
        return super().get_serializer_class()
