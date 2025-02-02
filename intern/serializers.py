from rest_framework import serializers
from .models import intern

class internSerializer(serializers.ModelSerializer):
    class Meta:
        model = intern
        fields = '__all__'
