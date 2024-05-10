from rest_framework import serializers
from .models import Jewellery_items

class Jewellery_itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewellery_items
        fields = '__all__'

    def create(serlf, validated_data):
        return Jewellery_items.objects.create(**validated_data)