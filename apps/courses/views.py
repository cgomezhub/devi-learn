from django.shortcuts import render
# Create your views here.

def course_list(request):
    return render(request, 'courses/courses.html')

def course_detail(request, course_id):
    return render(request, 'courses/course_detail.html', {
        'course': {'id': course_id, 'name': f'Course {course_id}', 'description': f'Description for Course {course_id}'}
    })

def course_lesson(request, course_id, lesson_id):
    return render(request, 'courses/lesson_detail.html', {
        'course_id': course_id,
        'lesson_id': lesson_id,
        'lesson': {'id': lesson_id, 'name': f'Lesson {lesson_id}'}
    })  
    