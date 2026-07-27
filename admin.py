from django.contrib import admin

from .models import (
    Course,
    Lesson,
    Enrollment,
    Learner,
    Question,
    Choice,
    Submission,
)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ("id", "question_text")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ("id", "title")


admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Learner)
admin.site.register(Choice)
admin.site.register(Submission)
