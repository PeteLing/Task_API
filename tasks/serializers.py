from rest_framework import serializers
from .models import Task, Tag


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    provider = serializers.ReadOnlyField(source='provider.username')
    acceptor = serializers.CharField(source='acceptor.username')
    tags = serializers.CharField(source='tags.name')

    class Meta:
        model = Task
        fields = ('id', 'title', 'detail', 'created_time', 'finished_time',
                  'excerpt', 'tags', 'provider', 'acceptor', 'status',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', )

