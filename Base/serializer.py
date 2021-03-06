from Base.models import User, Team, Content, Favourite, TeamMember, Comment
from . import models
from rest_framework import serializers


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class Fav_HisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False, allow_null=True, read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_favs = Fav_HisSerializer(many=True, required=False, allow_null=True, read_only=True)
    user_teams = TeamMemberSerializer(many=True, required=False, allow_null=True, read_only=True)
    user_contents = ContentSerializer(many=True, required=False, allow_null=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    team_peoples = TeamMemberSerializer(many=True, required=False, allow_null=True, read_only=True)
    team_contents = ContentSerializer(many=True, required=False, allow_null=True, read_only=True)

    # user_teams = UserSerializer(many=True, required=False, allow_null=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
