from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from electro_net.models import Supplier
from electro_net.serializer import SupplierSerializer


# Create your views here.

class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.level_up()


class SupplierListAPIView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]
