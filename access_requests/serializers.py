# access_requests/serializers.py

from rest_framework import serializers
from .models import AccessRequest


class AccessRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessRequest
        fields = '__all__'
        read_only_fields = ['requested_by', 'status']