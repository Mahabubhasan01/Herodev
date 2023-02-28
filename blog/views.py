import datetime
from django.shortcuts import render
from blog.models import Blog, Blog_Comment

# Create your views here.


def Home(request):
    blogs = Blog.objects.all()
    # Get the current date and time
    timenow = datetime.datetime.now()
    # Print the date and time in a custom format
    #print(timenow.strftime("%Y-%m-%d %H:%M:%S"))
    next = Blog.objects.filter(category='Next js')
    python = Blog.objects.filter(category='Python-django')
    context = {
        'time': timenow,
        'blogs': blogs,
        'next': next,
        'python': python,
    }

    return render(request, 'index.html', context)


def Blog_cat(request):
    blogs = Blog.objects.all()
    context = {
        'title': 'Blog | categories',
        'blogs': blogs
    }
    return render(request, 'category.html', context)


def FilterBy_cat(request, cat):
    blogs = Blog.objects.filter(category=cat)
    context = {
        'blogs': blogs,
        'category': cat
    }
    return render(request, 'bycategory.html', context)


def Blog_detail_Page(request, category, title, pk):
    blog = Blog.objects.get(id=pk)
    blogs = Blog.objects.filter(category=category)
    comments = Blog_Comment.objects.all()
    print(blogs)
    context = {
        'blogs': blogs,
        'blog': blog,
        'comments': comments,
        'titl': title,
        'cat': category,
    }
    return render(request, 'blog_detail.html', context)
number = 321
digit_sum = 0

# Convert number to string to access each digit
for digit in str(number):
    digit_sum += int(digit)

print(digit_sum)
