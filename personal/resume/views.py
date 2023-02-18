from django.shortcuts import render

from rest_framework import viewsets, permissions, pagination, generics, filters
from .serializers import ExperienceSerializer, EducationSerializer, CoursesSerializer, UserSerializer, \
    RegisterSerializer, CommentSerializer, ProjectsSerializer
from .models import Experience, Education, Courses, Comment, Projects
from rest_framework.response import Response


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    ordering = '-start'


class ExperienceViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['title', 'description', 'contest', 'company', 'skills__slug']
    ordering_fields = ['start']
    ordering = ['-start']
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class EducationView(generics.ListAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all().order_by('-date')
    lookup_field = 'university'
    permission_classes = [permissions.AllowAny]


class CoursesView(generics.ListAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all().order_by('-date')
    lookup_field = 'title'
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User has been successfully created",
        })


class AddCommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectsView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    permission_classes = [permissions.AllowAny]
