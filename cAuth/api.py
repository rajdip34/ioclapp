from cAuth.models import LoginData

from rest_framework import viewsets,permissions
from cAuth.serializers import LoginSerializer

# create login view set

class LoginViewSet(viewsets.ModelViewSet):
    queryset = LoginData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LoginSerializer
