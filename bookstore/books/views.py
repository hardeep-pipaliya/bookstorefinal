from django.shortcuts import render, HttpResponse


def index(request):
    data = {
        'title' : 'Django Book App'
    }
    return render(request, 'books/index.html', data)
