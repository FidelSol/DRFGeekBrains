from rest_framework import serializers
from .models import CustomUser

# Пользователь
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
        # user = CustomUser(
        #     email=validated_data['email'],
        #     username=validated_data['username'],
        #     first_name=validated_data['first_name'],
        #     last_name=validated_data['last_name'],
        # )
        # user.set_password(validated_data['password'])
        # user.save()
        # return user
        # user = CustomUser.objects.create_user(**validated_data)
        # return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.work_phone = validated_data.get('work_phone', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data and validated_data['password']:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance



