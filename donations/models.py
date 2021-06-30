from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class donations(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    reciever = models.ForeignKey(User, on_delete=models.CASCADE)
    Account_no = models.CharField(max_length=50, null=True, blank=True)
    Phone_number = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
