from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(required=False, max_length=1024)
    password = serializers.CharField(required=False, max_length=1024)
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail',
                                                read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'tasks')
