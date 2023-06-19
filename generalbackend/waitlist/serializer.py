from rest_framework import serializers
from .models import *
  
class waitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = waitlist
        fields = ['id', 'name', 'email', 'phone', 'position']