from django.db import models
from django.conf import settings

# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_with='course_images/')
    
    def __str__(self):
        return self.name

# Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=100, default="title")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

# TASK 1: Question Model
class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    mark = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

# TASK 1: Choice Model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

# TASK 1: Submission Model
class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

# Simple Enrollment model to satisfy the Submission ForeignKey
class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
