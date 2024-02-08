from django.urls import path
from . import views

urlpatterns=[
    path('',views.product_list, name='product-list'),
    path('create/',views.product_create,name='product-create'),
    path('<int:my_id>/',views.product_detail,name="product-detail"),
    path('<int:my_id>/update/',views.product_update,name="product-update"),
    path('<int:my_id>/delete/',views.product_delete,name="product-delete"),
]


