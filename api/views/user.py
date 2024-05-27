from rest_framework import generics, serializers, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        permission_classes = [permissions.IsAuthenticated]
        fields = ['id', 'username', 'email', 'role', 'password_hash', 'phone_number', 'address']
        extra_kwargs = {
            'password_hash': {'write_only': True}  # Ensure password hash is not readable
        }

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer