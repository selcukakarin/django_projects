from rest_framework import generics

# internal
from stok.models import Supplier, MaterialStock
from stok.api.serializers import (SupplierSerializer,
                                  StockSerializer,
                                  StockListSerializer,
                                  StockCreateSerializer,)


# class SupplierList(generics.ListAPIView):  # GET istekleri için
class SupplierList(generics.ListCreateAPIView):  # GET ve POST istekleri için
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class StockList(generics.ListCreateAPIView):
    queryset = MaterialStock.objects.all()
    serializer_class = StockSerializer


class StockListSeperated(generics.ListCreateAPIView):
    queryset = MaterialStock.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StockCreateSerializer
        return StockListSerializer


class StockDetail(generics.RetrieveUpdateAPIView):
    queryset = MaterialStock.objects.all()

    def get_serializer_class(self):
        return StockListSerializer

#
# class StockDetail(generics.RetrieveUpdateAPIView):
#     queryset = MaterialStock.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method == "PUT":
#             return StockCreateSerializer
#         return StockListSerializer

