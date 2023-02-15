from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    slug = models.SlugField()
    description = RichTextUploadingField()
    contest = RichTextUploadingField()
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    image = models.ImageField()
    link = models.CharField(max_length=200)
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = TaggableManager(verbose_name="skills")

    def __str__(self):
        return f"{self.title}, {self.company}"


class Education(models.Model):
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.university}"


class Courses(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.organization}"


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    company = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text


class ProLanguages(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class Technologies(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    link = models.CharField(max_length=200)
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pro_languages = models.ManyToManyField(ProLanguages)
    technologies = models.ManyToManyField(Technologies)

    def __str__(self):
        return f"{self.title}"



