from rest_framework import serializers
from .models import Modules


class ModulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modules
        fields = '__all__'
