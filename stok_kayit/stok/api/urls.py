from django.urls import path
# internal
from stok.api.routes import (SupplierList,
                             StockList,
                             StockListSeperated,
                             StockDetail)

urlpatterns = [
    path('suppliers/',
         SupplierList.as_view(),
         name='api-supplier-list'),
    path('stocks',
         StockList.as_view(),
         name='api-stock-list'),
    path('stocks-seperated',
         StockListSeperated.as_view(),
         name='api-stock-list-seperated'),
    path('stocks/<int:pk>',
         StockDetail.as_view(),
         name='api-stock-detail'),
]