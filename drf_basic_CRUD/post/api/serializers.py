from rest_framework import serializers
from post.models import Post


# Serializer exp
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(max_length=200)

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
            'created',
            'modified_by'
        ]
    def username_new(self, obj):
        return str(obj.user.username)
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #
    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)

    def create(self, validated_data):
        del validated_data["user"]
        return Post.objects.create(user=self.context["request"].user, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def validate_title(self, value):
        if value == "selçuk":
            raise serializers.ValidationError("Bu değer olmaz...")
        return value

    def validate(self, attrs):
        print(attrs["title"])
        if attrs["title"] == "selçuk2":
            raise serializers.ValidationError("olmaz")
        return attrs
