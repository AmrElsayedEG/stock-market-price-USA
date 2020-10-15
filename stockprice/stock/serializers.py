from rest_framework import serializers
from .models import DailyPrice


class DailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrice #Add model fields
        exclude = ['id'] #Add all fields to our serializer but not the id of the record