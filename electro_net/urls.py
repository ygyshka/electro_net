from django.urls import path

from electro_net.apps import ElectroNetConfig
from electro_net.views import (SupplierCreateAPIView, SupplierListAPIView,
                               SupplierRetrieveAPIView, SupplierUpdateAPIView,
                               SupplierDestroyAPIView)

app_name = ElectroNetConfig.name

urlpatterns = [

    path('supplier/create', SupplierCreateAPIView.as_view(), name='electro_net_create'),
    path('supplier', SupplierListAPIView.as_view(), name='electro_net_list'),
    path('supplier/<int:pk>', SupplierRetrieveAPIView.as_view(), name='electro_net_detail'),
    path('supplier/update/<int:pk>', SupplierUpdateAPIView.as_view(), name='electro_net_update'),
    path('supplier/destroy/<int:pk>', SupplierDestroyAPIView.as_view(), name='electro_net_delete'),
]
