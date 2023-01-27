from django.contrib.auth.models import User
from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )

    username = serializers.SerializerMethodField(method_name='username_new')

    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'content',
            'image',
            'url',
            'created_date',
            'modified_by'
        ]

    def username_new(self, obj):
        return str(obj.user.username)


class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image'
        ]

    # def create(self, validated_data):
    #
    #     validated_data["user"] = self.context["request"].user
    #     print(validated_data)
    #     return Post.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.title)
    #     instance.image = validated_data.get('image', instance.title)
    #     instance.save()
    #
    #     print("update")
    #     return instance

    # def validate_title(self, value):
    #     # title attribute'ü için değer kontrolü yaptık
    # we made a check for title variable
    #     if value == "selcuk":
    #         raise serializers.ValidationError("bvu değer olmaz")
    #     return value
    #
    # def validate(self, attrs):
    #     # tüm serializers datası için kontroller koyabiliriz.
    #     # we can check all of serializer data
    #     if attrs["title"] == "selcuk":
    #         raise serializers.ValidationError("olmaz")
    #     return attrs
