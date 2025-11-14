from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import Movie

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="Email already in use")])
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id','email','password','confirm_password','first_name','last_name')

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Password fields didn't match."})
        validate_password(attrs.get('password'))
        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.pop('password')
        validated_data.pop('confirm_password', None)
        first_name = validated_data.get('first_name','')
        last_name = validated_data.get('last_name','')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_at','user')

    def validate(self, attrs):
        title = attrs.get('title') or (self.instance.title if self.instance else None)
        if not title:
            raise serializers.ValidationError({"title":"Title is required."})

        media_type = attrs.get('media_type') or (self.instance.media_type if self.instance else None)
        total_eps = attrs.get('total_episodes') if 'total_episodes' in attrs else (self.instance.total_episodes if self.instance else None)
        episodes_watched = attrs.get('episodes_watched') if 'episodes_watched' in attrs else (self.instance.episodes_watched if self.instance else 0)

        if media_type == 'tv':
            if total_eps is None:
                raise serializers.ValidationError({"total_episodes":"Total episodes is required for TV shows."})
            try:
                if int(total_eps) <= 0:
                    raise serializers.ValidationError({"total_episodes":"Total episodes must be > 0."})
            except (ValueError, TypeError):
                raise serializers.ValidationError({"total_episodes":"Total episodes must be an integer > 0."})

        if episodes_watched is not None:
            try:
                ev = int(episodes_watched)
                if ev < 0:
                    raise serializers.ValidationError({"episodes_watched":"Episodes watched cannot be negative."})
                if total_eps is not None and ev > int(total_eps):
                    raise serializers.ValidationError({"episodes_watched":"Episodes watched cannot exceed total_episodes."})
            except (ValueError, TypeError):
                raise serializers.ValidationError({"episodes_watched":"Episodes watched must be an integer."})
        
        rating = attrs.get('rating') if 'rating' in attrs else (self.instance.rating if self.instance else None)
        if rating is not None:
            try:
                rv = float(rating)
                if rv < 1 or rv > 5:
                    raise serializers.ValidationError({"rating": "Rating must be between 1 and 5."})
            except (ValueError, TypeError):
                raise serializers.ValidationError({"rating": "Rating must be a number between 1 and 5."})

        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request,'user') and request.user.is_authenticated:
            validated_data['user'] = request.user
        if 'rating' in validated_data and validated_data['rating'] is not None:
            validated_data['rating'] = float(validated_data['rating'])
        return super().create(validated_data)