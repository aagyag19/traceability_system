from django.db import models

class Cooperative(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    registration_number = models.CharField(max_length=100, blank=True)
    established_date = models.DateField(null=True, blank=True)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    cooperative = models.ForeignKey(
        Cooperative,
        on_delete=models.CASCADE,
        related_name='farmers'
    )
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=20, default='kg')
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return self.name



class Delivery(models.Model):
    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name='deliveries'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='deliveries'
    )
    delivery_date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='kg')
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.farmer.name} - {self.product.name}"



class QualityCheck(models.Model):
    delivery = models.OneToOneField(
        Delivery,
        on_delete=models.CASCADE,
        related_name='quality_check'
    )
    checked_by = models.CharField(max_length=150)
    check_date = models.DateField()
    quality_grade = models.CharField(max_length=20)
    moisture = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    quantity_accepted = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.CharField(max_length=20)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Quality Check - {self.delivery}"


class Batch(models.Model):
    batch_number = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='batches'
    )
    deliveries = models.ManyToManyField(
        Delivery,
        related_name='batches'
    )
    batch_date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='kg')
    status = models.CharField(max_length=30, default='Created')
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.batch_number



class Processing(models.Model):
    batch = models.OneToOneField(
        Batch,
        on_delete=models.CASCADE,
        related_name='processing'
    )
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    processed_by = models.CharField(max_length=150, blank=True)
    process_description = models.TextField(blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Processing - {self.batch.batch_number}"


class Packaging(models.Model):
    batch = models.OneToOneField(
        Batch,
        on_delete=models.CASCADE,
        related_name='packaging'
    )
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    number_of_packages = models.PositiveIntegerField(null=True, blank=True)
    package_size = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    package_unit = models.CharField(max_length=20, default='kg')
    packaged_by = models.CharField(max_length=150, blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Packaging - {self.batch.batch_number}"


class Distribution(models.Model):
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name='distributions'
    )
    recipient_name = models.CharField(max_length=150)
    destination = models.CharField(max_length=200)
    dispatch_date = models.DateField()
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.batch.batch_number} - {self.recipient_name}"