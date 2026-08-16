from django.contrib import admin
from .models import (
    Cooperative,
    Farmer,
    Product,
    Delivery,
    QualityCheck,
    Batch,
    Processing,
    Packaging,
    Distribution,
)

admin.site.register(Cooperative)
admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(QualityCheck)
admin.site.register(Batch)
admin.site.register(Processing)
admin.site.register(Packaging)
admin.site.register(Distribution)