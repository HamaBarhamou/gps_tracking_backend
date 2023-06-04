from .models import User, Client
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.HyperlinkedRelatedField(view_name='user_management:client-detail', queryset=Client.objects.all(), required=False)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'role', 'client']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'name']