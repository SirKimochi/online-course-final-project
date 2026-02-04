from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

# Task 2: ChoiceInline implementation
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

# Task 2: QuestionInline implementation
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

# Task 2: QuestionAdmin implementation
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson']

# Task 2: LessonAdmin implementation
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# Registering the models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
