from django.urls import path, include
from rest_framework.routers import DefaultRouter
from resume.views import ExperienceViewSet, EducationView, CoursesView, ProfileView, RegisterView, AddCommentView, \
    ProjectsView #ProjectsViewSet


router = DefaultRouter()
router.register('experience', ExperienceViewSet, basename='experience')

urlpatterns = [
    path("", include(router.urls)),
    path("education/", EducationView.as_view()),
    path("courses/", CoursesView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('register/', RegisterView.as_view()),
    path("comments/", AddCommentView.as_view()),
    path("projects/", ProjectsView.as_view()),
]