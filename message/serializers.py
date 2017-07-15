from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message


class MessageSerializers(serializers.HyperlinkedModelSerializer):
    provider = serializers.ReadOnlyField(source='provider.username')

    class Meta:
        model = Message
        fields = ('id', 'title', 'detail', 'provider', 'created_time',)
