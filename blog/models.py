import uuid
import datetime
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Blog_Comment(models.Model):
    timenow = datetime.datetime.now()
    user = get_user_model()
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    commenter_name = models.ForeignKey(
        user, on_delete=models.CASCADE)
    commenter_image = models.ImageField(default='blank-profile-picture.png')
    comment_text = models.TextField(
        default='There is no people alive without dream')
    comment_post_date = models.DateTimeField(
        auto_now_add=True,)

    def __str__(self) -> str:
        return self.commenter_name.username


class Blog(models.Model):
    timenow = datetime.datetime.now()
    user = get_user_model()
    NEW_CHOICE = 'NC'
    MY_CHOICES = [
        ('choice_one', 'Choice One'),
        ('choice_two', 'Choice Two'),
        (NEW_CHOICE, 'New Choice'),  # new choice
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    author = models.ForeignKey(user, on_delete=models.CASCADE,)
    """ comments = models.ForeignKey(Comment, on_delete=models.CASCADE,) """
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    overview = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    code = models.TextField(blank=True)
    post_date = models.DateTimeField(
        auto_now_add=True,)
    update_date = models.DateTimeField(blank=True)
    tags = models.CharField(
        choices=MY_CHOICES, default='choice_one', max_length=20)

    def __str__(self) -> str:
        return self.title
