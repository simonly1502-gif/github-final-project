from django.contrib import admin
# 1. Import ĐỦ 7 CLASS theo đúng yêu cầu
from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner


# 2. Định nghĩa ChoiceInline (hiển thị Choice bên trong QuestionAdmin)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# 3. Định nghĩa QuestionInline (hiển thị Question bên trong CourseAdmin)
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


# 4. Định nghĩa QuestionAdmin (chứa ChoiceInline và list_display)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')


# 5. Định nghĩa LessonAdmin (chứa list_display)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


# 6. Định nghĩa CourseAdmin (BỔ SUNG - chứa QuestionInline và list_display)
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name', 'description')


# 7. Đăng ký các model với Django Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
