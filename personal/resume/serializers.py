from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from resume.models import Experience, Education, Courses, Comment, ProLanguages, Technologies, Projects


class ExperienceSerializer(TaggitSerializer, serializers.ModelSerializer):
    skills = TagListSerializerField()
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Experience
        fields = ("id", "title", "company", "slug", "description", "contest", "start", "end", "image", "link", "author", "skills")
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class EducationSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Education
        fields = ("id", "university", "degree", "field", "date", "image", "author")
        lookup_field = 'university'
        extra_kwargs = {
            'url': {'lookup_field': 'university'}
        }


class CoursesSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Courses
        fields = ("id", "title", "organization", "date", "image", "author")
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookup_field': 'title'}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passswords do not match!"})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class CommentSerializer(serializers.ModelSerializer):
    username = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ("id", "username", "company", "email", "text", "created_date")
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class ProLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProLanguages
        fields = ("title",)


class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = ("id", "title")


class ProjectsSerializer(serializers.ModelSerializer):
    pro_languages = serializers.SlugRelatedField(slug_field="title", queryset=ProLanguages.objects.all(), many=True)
    technologies = serializers.SlugRelatedField(slug_field="title", queryset=Technologies.objects.all(), many=True)

    class Meta:
        model = Projects
        fields = ("id", "title", "description", "link", "technologies", 'pro_languages')

