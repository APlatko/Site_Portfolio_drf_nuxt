from django.contrib import admin

from .models import Experience, Education, Courses, Comment, ProLanguages, Technologies, Projects


# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('skills')

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.skills.all())


class EducationAdmin(admin.ModelAdmin):
    pass


class CoursesAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


class ProjectsAdmin(admin.ModelAdmin):
    pass


class ProLanguagesAdmin(admin.ModelAdmin):
    pass


class TechnologiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(ProLanguages, ProLanguagesAdmin)
admin.site.register(Technologies, TechnologiesAdmin)
admin.site.register(Projects, ProjectsAdmin)
