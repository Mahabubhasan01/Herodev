from msilib.schema import Class
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.


class Blog(models.Model):
    user = get_user_model()
    NEW_CHOICE = 'NC'
    MY_CHOICES = [
        ('choice_one', 'Choice One'),
        ('choice_two', 'Choice Two'),
        (NEW_CHOICE, 'New Choice'),  # new choice
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    author = models.ForeignKey(user, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    overview = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    code = models.CharField(max_length=33)
    post_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True)
    tags = models.CharField(
        choices=MY_CHOICES, default='choice_one', max_length=20)
