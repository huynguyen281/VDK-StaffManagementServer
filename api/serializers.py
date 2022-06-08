from dataclasses import field
from rest_framework import serializers
from managerApp.models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'code', 'name', 'age', 'gender')