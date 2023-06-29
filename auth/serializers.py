from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class TokenObtainPairResponseSerializer(TokenObtainPairSerializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField(read_only=True)
    groups = serializers.ListField(read_only=True)

    class Meta:
        exclude = ('password')

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        # Add extra responses here
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['groups'] = self.user.groups.values_list('name', flat=True)
        # self(data)
        return data

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
        extra_kwargs = {

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'id', 'email']
