from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from academiaCore.models import UserProfile, TYPE_OF_USER

class UserProfileSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user = serializers.OneToOneField(read_only=True)
    user_type = serializers.ChoiceField(choices=TYPE_OF_USER, required=True)
    birthday = serializers.DateField(required=True)
    pic = serializers.ImageField(required=False)

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.pic = validated_data.get('pic', instance.pic)
        instance.save()
        return instance