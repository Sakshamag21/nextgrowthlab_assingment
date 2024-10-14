from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    file = models.FileField(default='default.jpg',upload_to='uploaded_files/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    points_allotted = models.IntegerField(default=0)
    
    def __str__(self):
        return self.file.name
