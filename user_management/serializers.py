from .models import User, Client
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


""" class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Ajoutez des informations supplémentaires au token
        token['username'] = user.username
        # Ajoutez d'autres champs si nécessaire
        return token """
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Ajouter les informations supplémentaires de l'utilisateur
        user = self.user
        data['user_id'] = user.id
        data['username'] = user.username
        data['email'] = user.email
        data['role'] = user.role
        client_serializer = ClientSerializer(user.client)
        data['client'] = client_serializer.data
        
        # Renommer la clé "access" en "token"
        data['token'] = data.pop('access')
        
        return data

class UserSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.HyperlinkedRelatedField(view_name='user_management:client-detail', queryset=Client.objects.all(), required=False)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'role', 'client']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'name']