# Generated by Django 4.1.5 on 2023-01-14 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('commenter_image', models.ImageField(default='blank-profile-picture.png', upload_to='')),
                ('comment_text', models.TextField(default='There is no people alive without dream')),
                ('comment_post_date', models.DateTimeField(auto_now_add=True)),
                ('commenter_name', models.ForeignKey(default='There is no people alive without dream', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
                ('code', models.TextField(blank=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True)),
                ('tags', models.CharField(choices=[('choice_one', 'Choice One'), ('choice_two', 'Choice Two'), ('NC', 'New Choice')], default='choice_one', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
