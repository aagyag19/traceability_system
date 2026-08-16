from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path(
        'cooperatives/',
        views.cooperative_list,
        name='cooperative_list'
    ),

    path(
        'cooperatives/add/',
        views.cooperative_create,
        name='cooperative_create'
    ),

    path(
        'cooperatives/<int:pk>/edit/',
        views.cooperative_update,
        name='cooperative_update'
    ),

    path(
        'cooperatives/<int:pk>/delete/',
        views.cooperative_delete,
        name='cooperative_delete'
    ),

    path(
        'farmers/',
        views.farmer_list,
        name='farmer_list'
    ),

    path(
        'farmers/add/',
        views.farmer_create,
        name='farmer_create'
    ),

    path(
        'farmers/<int:pk>/edit/',
        views.farmer_update,
        name='farmer_update'
    ),

    path(
        'farmers/<int:pk>/delete/',
        views.farmer_delete,
        name='farmer_delete'
    ),


    path(
        'products/',
        views.product_list,
        name='product_list'
    ),

    path(
        'products/add/',
        views.product_create,
        name='product_create'
    ),

    path(
        'products/',
        views.product_list,
        name='product_list'
    ),

    path(
        'products/add/',
        views.product_create,
        name='product_create'
    ),

    path(
        'products/<int:pk>/edit/',
        views.product_update,
        name='product_update'
    ),

    path(
        'products/<int:pk>/delete/',
        views.product_delete,
        name='product_delete'
    ),

    path(
        'deliveries/',
        views.delivery_list,
        name='delivery_list'
    ),

    path(
        'deliveries/add/',
        views.delivery_create,
        name='delivery_create'
    ),

    path(
        'deliveries/<int:pk>/edit/',
        views.delivery_update,
        name='delivery_update'
    ),

    path(
        'deliveries/<int:pk>/delete/',
        views.delivery_delete,
        name='delivery_delete'
    ),

    path(
        'quality-checks/',
        views.quality_check_list,
        name='quality_check_list'
    ),

    path(
        'quality-checks/add/',
        views.quality_check_create,
        name='quality_check_create'
    ),

    path(
        'quality-checks/<int:pk>/edit/',
        views.quality_check_update,
        name='quality_check_update'
    ),

    path(
        'quality-checks/<int:pk>/delete/',
        views.quality_check_delete,
        name='quality_check_delete'
    ),

    path(
        'batches/',
        views.batch_list,
        name='batch_list'
    ),

    path(
        'batches/add/',
        views.batch_create,
        name='batch_create'
    ),

    path(
        'batches/<int:pk>/edit/',
        views.batch_update,
        name='batch_update'
    ),

    path(
        'batches/<int:pk>/delete/',
        views.batch_delete,
        name='batch_delete'
    ),

    path(
        'processing/',
        views.processing_list,
        name='processing_list'
    ),

    path(
        'processing/add/',
        views.processing_create,
        name='processing_create'
    ),

    path(
        'processing/<int:pk>/edit/',
        views.processing_update,
        name='processing_update'
    ),

    path(
        'processing/<int:pk>/delete/',
        views.processing_delete,
        name='processing_delete'
    ),

    path(
        'packaging/',
        views.packaging_list,
        name='packaging_list'
    ),

    path(
        'packaging/add/',
        views.packaging_create,
        name='packaging_create'
    ),

    path(
        'packaging/<int:pk>/edit/',
        views.packaging_update,
        name='packaging_update'
    ),

    path(
        'packaging/<int:pk>/delete/',
        views.packaging_delete,
        name='packaging_delete'
    ),

    path(
        'distribution/',
        views.distribution_list,
        name='distribution_list'
    ),

    path(
        'distribution/add/',
        views.distribution_create,
        name='distribution_create'
    ),

    path(
        'distribution/<int:pk>/edit/',
        views.distribution_update,
        name='distribution_update'
    ),

    path(
        'distribution/<int:pk>/delete/',
        views.distribution_delete,
        name='distribution_delete'
    ),
]