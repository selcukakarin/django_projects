from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    # username = serializers.SerializerMethodField(method_name='username_new')
    username = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'username',
            'user',
            'title',
            'content',
            'image',
            'url',
            'slug',
            'created',
            'modified_by'
        ]

    # def username_new(self, obj):
    #     return str(obj.user.username)

    def get_username(self, obj):
        return str(obj.user.username)


class PostUpdateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]

    # def save(self, **kwargs):
    # duruma göre ya update ya da create metodunu çalıştırır
    #     return True

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.title)
    #     instance.image = validated_data.get('image', instance.title)
    #     instance.save()
    #     return instance

    # def create(self, validated_data):
    #     return Post.objects.create(user = self.context["request"].user, **validated_data)

    # def validate(self, attrs):
    #     if attrs['title'] == "selcuk":
    #         raise serializers.ValidationError("olmaz")
    #     return attrs

    # def validate_title(self, value):
    #     if value == "selçuk":
    #         raise serializers.ValidationError("Bu değer girilemez")
    #     return value