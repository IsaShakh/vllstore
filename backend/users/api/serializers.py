from rest_framework import serializers
from users.models import User
from products.api.serializers import ProductSerializer


class RegisterUserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return self.perform_create(**validated_data)
    
    def perform_create(self, email, **validated_data):
        email = User.objects.normalize_email(email)
        user = User(email=email, **validated_data)
        user.set_unusable_password
        user.save()
        return user
    
    class Meta:
        model = User
        fields = [
            'email',
        ]
        extra_kwargs = {
            'email' : {'required':True}
        }


class UserProfileSerializer(serializers.ModelSerializer):
    owned_positions = ProductSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'phone',
            'birthday',
            'first_name',
            'second_name',
            'profile_photo',
            'is_superuser',
            'email_verified',
        ]
        read_only_fields = [
            'email',
        ]