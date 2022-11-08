from rest_framework import serializers
from ..models import Account

class UserProfileSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'passowrd'}, write_only=True)
    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'name', 'password', 'password2', 'picture', 'last_login',]
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only':True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords must match!'})
        account.set_password(password)
        account.save()
        return account

class UserProfileDetailedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = [ 'email', 'username', 'name', 'picture']
