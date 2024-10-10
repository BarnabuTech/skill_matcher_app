# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    skills_required = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.TextField(help_text="Comma-separated list of skills")
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Job Alert"
