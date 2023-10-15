from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    email_id = serializers.CharField(required=True, max_length=256)
    password = serializers.CharField(required=True, max_length=256)


class UserCreateSerializer(UserLoginSerializer):
    full_name = serializers.CharField(required=True, max_length=256)
    is_active = serializers.BooleanField(required=False)
    is_admin = serializers.BooleanField(required=False)


class PostCreateSerializer(serializers.Serializer):
    post_content = serializers.CharField(required=True, max_length=1024)
