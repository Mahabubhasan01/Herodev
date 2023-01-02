from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'index.html')


def Blog_cat(request):
    context = {
        'title': 'Blog | categories'
    }
    return render(request, 'category.html', context)


def Blog_detail(request):
    return render(request, 'single.html')
