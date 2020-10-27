from .models import Data_Set
from rest_framework import serializers


class DataSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data_Set
        fields = ('grol','id')