from django.db import models
from django.conf import settings
from .category import Category

class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner_courses')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='CourseCategory', related_name='courses')
    image = models.CharField(max_length=200, blank=True)
    level = models.CharField(max_length=200, blank=True)
    rating = models.FloatField(default=0.0)
    duration = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)

    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class CourseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('course', 'category')

    def __str__(self):
        return self.course.title + ' - ' + self.category.name
