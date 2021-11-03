from rest_framework import serializers
from .models import Project, ToDo
from apipoint.models import CustomUser

class PresentProjectSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Project
        fields = ['id', 'name', 'url', 'users']


class CRUDProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=False, allow_null=True)

    class Meta:
        model = Project
        fields = ['__all__']

class PresentToDoSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1500, required=False)
    project = serializers.StringRelatedField(required=False)
    creator = serializers.StringRelatedField(required=False)
    add_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")
    mod_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")

    class Meta:
        model = ToDo
        fields = ['__all__']


class CRUDToDoSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1500, required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False, allow_null=True)
    creator = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    add_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")
    mod_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")

    class Meta:
        model = ToDo
        fields = ['__all__']






