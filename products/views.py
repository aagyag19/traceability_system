from django.shortcuts import render, redirect, get_object_or_404
from .models import(
     Cooperative, 
     Farmer, 
     Product, 
     Delivery, 
     QualityCheck, 
     Batch, 
     Processing, 
     Packaging, 
     Distribution
)
from django.contrib.auth.decorators import login_required
from .forms import (
    CooperativeForm,
    FarmerForm,
    ProductForm,
    DeliveryForm,
    QualityCheckForm,
    BatchForm,
    ProcessingForm,
    PackagingForm,
    DistributionForm
)
import qrcode
from io import BytesIO
from django.http import HttpResponse

def home(request):
    return render(request, 'public/home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def cooperative_list(request):
    cooperatives = Cooperative.objects.all()
    return render(
        request,
        'cooperatives/cooperative_list.html',
        {'cooperatives': cooperatives}
    )

@login_required
def cooperative_create(request):
    if request.method == 'POST':
        form = CooperativeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cooperative_list')
    else:
        form = CooperativeForm()

    return render(
        request,
        'cooperatives/cooperative_form.html',
        {'form': form}
    )


@login_required
def cooperative_update(request, pk):
    cooperative = Cooperative.objects.get(pk=pk)

    if request.method == 'POST':
        form = CooperativeForm(request.POST, instance=cooperative)

        if form.is_valid():
            form.save()
            return redirect('cooperative_list')
    else:
        form = CooperativeForm(instance=cooperative)

    return render(
        request,
        'cooperatives/cooperative_form.html',
        {
            'form': form,
            'cooperative': cooperative
        }
    )

@login_required
def cooperative_delete(request, pk):
    cooperative = Cooperative.objects.get(pk=pk)

    if request.method == 'POST':
        cooperative.delete()
        return redirect('cooperative_list')

    return render(
        request,
        'cooperatives/cooperative_confirm_delete.html',
        {'cooperative': cooperative}
    )

@login_required
def farmer_list(request):
    farmers = Farmer.objects.select_related('cooperative').all()

    return render(
        request,
        'farmers/farmer_list.html',
        {'farmers': farmers}
    )

@login_required
def farmer_create(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerForm()

    return render(
        request,
        'farmers/farmer_form.html',
        {'form': form}
    )

@login_required
def farmer_update(request, pk):
    farmer = Farmer.objects.get(pk=pk)

    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)

        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerForm(instance=farmer)

    return render(
        request,
        'farmers/farmer_form.html',
        {
            'form': form,
            'farmer': farmer
        }
    )

@login_required
def farmer_delete(request, pk):
    farmer = Farmer.objects.get(pk=pk)

    if request.method == 'POST':
        farmer.delete()
        return redirect('farmer_list')

    return render(
        request,
        'farmers/farmer_confirm_delete.html',
        {'farmer': farmer}
    )


@login_required
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(
        request,
        'products/product_form.html',
        {'form': form}
    )

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'products/product_form.html',
        {
            'form': form,
            'product': product
        }
    )

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(
        request,
        'products/product_confirm_delete.html',
        {'product': product}
    )

@login_required
def delivery_list(request):
    deliveries = Delivery.objects.select_related(
        'farmer',
        'product'
    ).all()

    return render(
        request,
        'deliveries/delivery_list.html',
        {'deliveries': deliveries}
    )


@login_required
def delivery_create(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm()

    return render(
        request,
        'deliveries/delivery_form.html',
        {'form': form}
    )

@login_required
def delivery_update(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)

    if request.method == 'POST':
        form = DeliveryForm(
            request.POST,
            instance=delivery
        )

        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm(instance=delivery)

    return render(
        request,
        'deliveries/delivery_form.html',
        {
            'form': form,
            'delivery': delivery
        }
    )

@login_required
def delivery_delete(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)

    if request.method == 'POST':
        delivery.delete()
        return redirect('delivery_list')

    return render(
        request,
        'deliveries/delivery_confirm_delete.html',
        {'delivery': delivery}
    )

@login_required
def quality_check_list(request):
    quality_checks = QualityCheck.objects.select_related(
        'delivery',
        'delivery__farmer',
        'delivery__product'
    ).all()

    return render(
        request,
        'quality_checks/quality_check_list.html',
        {'quality_checks': quality_checks}
    )

@login_required
def quality_check_create(request):
    if request.method == 'POST':
        form = QualityCheckForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('quality_check_list')
    else:
        form = QualityCheckForm()

    return render(
        request,
        'quality_checks/quality_check_form.html',
        {'form': form}
    )

@login_required
def quality_check_update(request, pk):
    quality_check = get_object_or_404(
        QualityCheck,
        pk=pk
    )

    if request.method == 'POST':
        form = QualityCheckForm(
            request.POST,
            instance=quality_check
        )

        if form.is_valid():
            form.save()
            return redirect('quality_check_list')
    else:
        form = QualityCheckForm(
            instance=quality_check
        )

    return render(
        request,
        'quality_checks/quality_check_form.html',
        {
            'form': form,
            'quality_check': quality_check
        }
    )

@login_required
def quality_check_delete(request, pk):
    quality_check = get_object_or_404(
        QualityCheck,
        pk=pk
    )

    if request.method == 'POST':
        quality_check.delete()
        return redirect('quality_check_list')

    return render(
        request,
        'quality_checks/quality_check_confirm_delete.html',
        {'quality_check': quality_check}
    )

@login_required
def batch_list(request):
    batches = Batch.objects.select_related(
        'product'
    ).prefetch_related(
        'deliveries'
    ).all()

    return render(
        request,
        'batches/batch_list.html',
        {'batches': batches}
    )

@login_required
def batch_create(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('batch_list')
    else:
        form = BatchForm()

    return render(
        request,
        'batches/batch_form.html',
        {'form': form}
    )

@login_required
def batch_update(request, pk):
    batch = get_object_or_404(Batch, pk=pk)

    if request.method == 'POST':
        form = BatchForm(
            request.POST,
            instance=batch
        )

        if form.is_valid():
            form.save()
            return redirect('batch_list')
    else:
        form = BatchForm(instance=batch)

    return render(
        request,
        'batches/batch_form.html',
        {
            'form': form,
            'batch': batch
        }
    )

@login_required
def batch_delete(request, pk):
    batch = get_object_or_404(Batch, pk=pk)

    if request.method == 'POST':
        batch.delete()
        return redirect('batch_list')

    return render(
        request,
        'batches/batch_confirm_delete.html',
        {'batch': batch}
    )

@login_required
def processing_list(request):
    processings = Processing.objects.select_related(
        'batch',
        'batch__product'
    ).all()

    return render(
        request,
        'processing/processing_list.html',
        {'processings': processings}
    )


@login_required
def processing_create(request):
    if request.method == 'POST':
        form = ProcessingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('processing_list')
    else:
        form = ProcessingForm()

    return render(
        request,
        'processing/processing_form.html',
        {'form': form}
    )

@login_required
def processing_update(request, pk):
    processing = get_object_or_404(
        Processing,
        pk=pk
    )

    if request.method == 'POST':
        form = ProcessingForm(
            request.POST,
            instance=processing
        )

        if form.is_valid():
            form.save()
            return redirect('processing_list')
    else:
        form = ProcessingForm(
            instance=processing
        )

    return render(
        request,
        'processing/processing_form.html',
        {
            'form': form,
            'processing': processing
        }
    )

@login_required
def processing_delete(request, pk):
    processing = get_object_or_404(
        Processing,
        pk=pk
    )

    if request.method == 'POST':
        processing.delete()
        return redirect('processing_list')

    return render(
        request,
        'processing/processing_confirm_delete.html',
        {'processing': processing}
    )

@login_required
def packaging_list(request):
    packagings = Packaging.objects.select_related(
        'batch',
        'batch__product'
    ).all()

    return render(
        request,
        'packaging/packaging_list.html',
        {'packagings': packagings}
    )

@login_required
def packaging_create(request):
    if request.method == 'POST':
        form = PackagingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('packaging_list')
    else:
        form = PackagingForm()

    return render(
        request,
        'packaging/packaging_form.html',
        {'form': form}
    )

@login_required
def packaging_update(request, pk):
    packaging = get_object_or_404(
        Packaging,
        pk=pk
    )

    if request.method == 'POST':
        form = PackagingForm(
            request.POST,
            instance=packaging
        )

        if form.is_valid():
            form.save()
            return redirect('packaging_list')
    else:
        form = PackagingForm(
            instance=packaging
        )

    return render(
        request,
        'packaging/packaging_form.html',
        {
            'form': form,
            'packaging': packaging
        }
    )

@login_required
def packaging_delete(request, pk):
    packaging = get_object_or_404(
        Packaging,
        pk=pk
    )

    if request.method == 'POST':
        packaging.delete()
        return redirect('packaging_list')

    return render(
        request,
        'packaging/packaging_confirm_delete.html',
        {'packaging': packaging}
    )

@login_required
def distribution_list(request):
    distributions = Distribution.objects.select_related(
        'batch',
        'batch__product'
    ).all()

    return render(
        request,
        'distribution/distribution_list.html',
        {'distributions': distributions}
    )

@login_required
def distribution_create(request):
    if request.method == 'POST':
        form = DistributionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('distribution_list')
    else:
        form = DistributionForm()

    return render(
        request,
        'distribution/distribution_form.html',
        {'form': form}
    )

@login_required
def distribution_update(request, pk):
    distribution = get_object_or_404(
        Distribution,
        pk=pk
    )

    if request.method == 'POST':
        form = DistributionForm(
            request.POST,
            instance=distribution
        )

        if form.is_valid():
            form.save()
            return redirect('distribution_list')
    else:
        form = DistributionForm(
            instance=distribution
        )

    return render(
        request,
        'distribution/distribution_form.html',
        {
            'form': form,
            'distribution': distribution
        }
    )

@login_required
def distribution_delete(request, pk):
    distribution = get_object_or_404(
        Distribution,
        pk=pk
    )

    if request.method == 'POST':
        distribution.delete()
        return redirect('distribution_list')

    return render(
        request,
        'distribution/distribution_confirm_delete.html',
        {'distribution': distribution}
    )


def verify_batch(request):
    batch = None
    batch_number = request.GET.get('batch_number')

    if batch_number:
        try:
            batch = Batch.objects.select_related(
                'product'
            ).prefetch_related(
                'deliveries__farmer__cooperative'
            ).get(
                batch_number=batch_number
            )
        except Batch.DoesNotExist:
            batch = None

    quality_check = None
    processing = None
    packaging = None
    distributions = []

    if batch:
        # Get quality check from the deliveries used in this batch
        for delivery in batch.deliveries.all():
            try:
                quality_check = delivery.quality_check
                break
            except QualityCheck.DoesNotExist:
                continue

        # Get processing record
        try:
            processing = batch.processing
        except Processing.DoesNotExist:
            processing = None

        # Get packaging record
        try:
            packaging = batch.packaging
        except Packaging.DoesNotExist:
            packaging = None

        # Get distribution records
        distributions = batch.distributions.all()

    return render(
        request,
        'public/verify_batch.html',
        {
            'batch': batch,
            'batch_number': batch_number,
            'quality_check': quality_check,
            'processing': processing,
            'packaging': packaging,
            'distributions': distributions,
        }
    )

@login_required
def batch_qr(request, pk):
    batch = get_object_or_404(Batch, pk=pk)

    verification_url = request.build_absolute_uri(
        f'/verify/?batch_number={batch.batch_number}'
    )

    qr = qrcode.make(verification_url)

    buffer = BytesIO()
    qr.save(buffer, format='PNG')

    return HttpResponse(
        buffer.getvalue(),
        content_type='image/png'
    )