from rest_framework import viewsets

from .serializers import DataSetSerializer
from .models import Data_Set


class DataSetViewSet(viewsets.ModelViewSet):
    queryset = Data_Set.objects.all().order_by('id')
    serializer_class = DataSetSerializer