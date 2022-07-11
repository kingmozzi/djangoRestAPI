from .models import Practice
from rest_framework import serializers, viewsets

class PracticeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Practice
        fields = ['id', 'name', 'uid', 'age']