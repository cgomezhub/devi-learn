from django.db import models
from django.conf import settings

class InstructorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instructor_profile')
    bio = models.TextField(blank=True, null=True)
    photo = models.URLField(blank=True, null=True)    
    website = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    social_networ = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username or self.user.get_full_name()