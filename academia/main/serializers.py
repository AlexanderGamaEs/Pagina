from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import SectionMainPage

class SectionMainPageSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    last_edition = serializers.DateField(required=True)

    def create(self, validated_data):
        return SectionMainPage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.last_edition = validated_data.get('last_edition', instance.last_edition)
        instance.save()
        return instance