from rest_framework import serializers
from cAuth.models import LoginData

# create serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginData
        fields = '__all__'

