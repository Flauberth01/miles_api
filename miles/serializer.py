from rest_framework import serializers
from miles.models import Depoimento


class DepoimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = '__all__'
