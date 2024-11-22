from rest_framework import serializers
from django.db import transaction
from . import models


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceDetail
        exclude = ["invoice"]

    def validate(self, attrs):
        if attrs['quantity'] <= 0:
            raise serializers.ValidationError({"quantity": "please enter a number greater than zero"})
        if attrs['price'] <= 0:
            raise serializers.ValidationError({"price": "please enter a number greater than zero"})
        if attrs['line_total'] <= 0:
            raise serializers.ValidationError({"line_total": "please enter a number greater than zero"})
        return super().validate(attrs)


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(source="invoicedetail_set", many=True, read_only=True)

    class Meta:
        model = models.Invoice
        fields = "__all__"


class CreateInvoiceSerializer(InvoiceSerializer):
    details = InvoiceDetailSerializer(many=True, write_only=True, required=True)

    @transaction.atomic
    def create(self, validated_data):
        details = validated_data.pop("details")
        invoice = super().create(validated_data)
        self.create_invoice_details(invoice, details)
        return invoice

    @transaction.atomic
    def update(self, instance, validated_data):
        details = validated_data.pop("details")
        instance = super().update(instance, validated_data)
        models.InvoiceDetail.objects.filter(invoice=instance).delete()
        self.create_invoice_details(instance, details)
        return instance

    def create_invoice_details(self, invoice, details):
        models.InvoiceDetail.objects.bulk_create(
            [
                models.InvoiceDetail(
                    invoice=invoice,
                    description=detail["description"],
                    quantity=detail["quantity"],
                    price=detail["price"],
                    line_total=detail["line_total"]
                    )
                for detail in details
            ]
        )
