from django.contrib import admin

from blog.models import Blog,Blog_Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Blog_Comment)
