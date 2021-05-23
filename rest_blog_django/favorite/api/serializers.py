from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from favorite.models import Favorite


class FavoriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def validate(self, attrs):
        queryset = Favorite.objects.filter(post=attrs["post"], user=attrs["user"])
        if queryset.exists:
            raise serializers.ValidationError("Zaten favlara eklendi")
        return attrs


class FavoriteAPISerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('content',)
