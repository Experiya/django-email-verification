from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    is_approve = models.BooleanField(default=False)
    auth_token=models.CharField(max_length=200)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user.username