from rest_framework import serializers
from .models import Venda

class MinhaTabelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
