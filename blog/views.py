import datetime
from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def Home(request):

    # Get the current date and time
    timenow = datetime.datetime.now()

    # Print the date and time in a custom format
    print(timenow.strftime("%Y-%m-%d %H:%M:%S"))
    context = {
        'time': timenow
    }

    return render(request, 'index.html', context)


def Blog_cat(request):
    context = {
        'title': 'Blog | categories'
    }
    return render(request, 'category.html', context)


def Blog_detail(request):
    return render(request, 'single.html')
