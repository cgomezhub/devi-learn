
from django.db import models
from django.conf import settings
from .course import Course

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    # completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'course')
        
    def __str__(self):
        return f'{self.user.username} inscrito en el curso: - {self.course.title}'

    
