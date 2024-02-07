from django.urls import path
from . import views

urlpatterns=[
    path("product/",views.product_detail,name="product"),
    path('create/',views.product_create,name='create'),
    path('products/<int:my_id>/',views.dynamic_look,name="product-detail"),
    path('products/<int:my_id>/delete/',views.product_delete,name="product-delete"),
    path('products/',views.product_list, name='product-list')
]


