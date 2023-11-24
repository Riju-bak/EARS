from django.contrib import admin
from .models import JobApplication, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class JobApplicationAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


# Register your models here.
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Comment)
