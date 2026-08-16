from django import forms
from .models import Cooperative, Farmer, Product, Delivery, QualityCheck, Batch, Processing, Packaging, Distribution


class CooperativeForm(forms.ModelForm):
    class Meta:
        model = Cooperative
        fields = [
            'name',
            'address',
            'contact',
            'email',
            'registration_number',
            'established_date',
            'certifications',
        ]


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = [
            'cooperative',
            'name',
            'address',
            'contact',
            'email',
            'date_of_birth',
            'status',
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'description',
            'unit',
            'status',
        ]

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'farmer',
            'product',
            'delivery_date',
            'quantity',
            'unit',
            'remarks',
        ]

class QualityCheckForm(forms.ModelForm):
    class Meta:
        model = QualityCheck
        fields = [
            'delivery',
            'checked_by',
            'check_date',
            'quality_grade',
            'moisture',
            'quantity_accepted',
            'status',
            'remarks',
        ]

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            'batch_number',
            'product',
            'deliveries',
            'batch_date',
            'quantity',
            'unit',
            'status',
            'remarks',
        ]

class ProcessingForm(forms.ModelForm):
    class Meta:
        model = Processing
        fields = [
            'batch',
            'started_at',
            'completed_at',
            'status',
            'processed_by',
            'process_description',
            'remarks',
        ]

class PackagingForm(forms.ModelForm):
    class Meta:
        model = Packaging
        fields = [
            'batch',
            'started_at',
            'completed_at',
            'status',
            'number_of_packages',
            'package_size',
            'package_unit',
            'packaged_by',
            'remarks',
        ]

class DistributionForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = [
            'batch',
            'recipient_name',
            'destination',
            'dispatch_date',
            'delivery_date',
            'status',
            'remarks',
        ]