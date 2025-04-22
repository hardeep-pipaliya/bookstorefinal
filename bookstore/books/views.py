from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from books.models import Book, Reviews
# import json
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from books.form import ReviewForm
# with open('D:/python/bookstore-project/bookstore/books.json', 'r') as file:
#     jdata = json.load(file)   


# @staff_member_required
def index(request):
    modeldata = Book.objects.all()
    data = {
        'jdata' : modeldata,        
    }
    return render(request, 'books/index.html', data)

# def show(request, id):
#     singlebook = list()
#     for book in jdata:
#         if book['id'] == id:
#             singlebook = book
#     data = {
#         'jdata' : singlebook,        
#     }
#     return render(request, "books/show.html", data)
# @login_required

def show(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Reviews.objects.filter(book=book).order_by('-created_date')
    form = ReviewForm()
    jdata = {
        'jdata': book,
        'reviews': reviews,
        'user': request.user,
        'form' : form
    }
    return render(request, 'books/show.html', jdata)


# @login_required
@csrf_exempt
def review(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            book = get_object_or_404(Book, id=id)
            form = ReviewForm(request.POST)
            if form.is_valid():
                review_instance = form.save(commit=False)
                review_instance.user = request.user
                review_instance.book = book  # ✅ Link the review to the correct book
                review_instance.save()
                return redirect('show', id=id)
            else:
                return HttpResponse("Form is not valid", status=400)
    return HttpResponse("Invalid Method", status=405)



