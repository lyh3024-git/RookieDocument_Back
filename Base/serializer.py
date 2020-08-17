from Base.models import User, Team, Content, Fav_His
from . import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class Fav_HisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fav_His
        fields = '__all__'

