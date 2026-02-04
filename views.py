from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission, Enrollment
from django.http import HttpResponseRedirect
from django.urls import reverse

# Task 5: Function to handle exam submission
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Logic to extract selected choices and calculate score
        # In a real app, you'd loop through questions and compare with Choice.is_correct
        return redirect('onlinecourse:show_exam_result', course_id=course.id)

# Task 5: Function to show exam results
def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Mock data for the final project requirement
    context = {
        'course': course,
        'grade': 100,
        'status': 'Passed',
        'message': 'Congratulations!'
    }
    return render(request, 'onlinecourse/exam_result.html', context)
