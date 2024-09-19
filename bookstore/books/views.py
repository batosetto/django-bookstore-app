from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import BookForm, ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def books(request):
    books = Book.objects.all()

    context = {
        "page_title": "Books",
        "books": books
    }

    return render(request, 'homepage.html', context)

def book(request, pk):
    book = Book.objects.get(id=pk)
    reviews = book.reviews.all()

    context = {
        "page_title": book.title,
        "book": book,
        "reviews": reviews
    }

    return render(request, 'book.html', context)

@login_required(login_url='login')
def addBook(request):
    form = BookForm()

    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            description=request.POST.get('description'),
            year=request.POST.get('year'),
            rating=request.POST.get('rating'),
            posted_by=request.user
        )

        return redirect("/")
    
    context = {
        "page_title": "Add Book",
        "form": form
    }

    return render(request, 'book_add.html', context)

@login_required(login_url='login')
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if(book.posted_by != request.user):
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.year = request.POST.get('year')
        book.rating = request.POST.get('rating')
        book.save()

        # return redirect("/book/" + str(pk))
        return redirect("/")
    
    context = {
        "page_title": "Update Book",
        # "book": book,
        "form": form
    }

    return render(request, 'book_add.html', context)

@login_required(login_url='login')
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if book.posted_by != request.user:
        return render(render, "not_authorized.html")
    
    if (request.method == "POST"):
        book.delete()
        return redirect("/")

    context ={
        "book": book,
    }

    return render(request, "delete.html", context)

@login_required(login_url='login')
def addReview(request, pk):
    book = Book.objects.get(id=pk)
    form = ReviewForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.posted_by = request.user
        review.save()
        return redirect('/')

    context = {
        'book_id': pk, 
        "page_title": "Review Book",
        "form": form
    }

    return render(request, "review_add.html", context)

def review_detail(request, pk):
    review = Review.objects.get(id=pk)

    context = {
        'review': review,

    }

    return render(request, 'review_detail.html', context)

@login_required(login_url='login')
def review_edit(request, pk):
    review = Review.objects.get(id=pk)

    if review.posted_by != request.user:
        return render(request, "not_authorized.html")

    form = ReviewForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('review_detail', pk=review.id)

    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'review_edit.html', context)

@login_required(login_url='login')
def review_delete(request, pk):
    review = Review.objects.get(id=pk)

    if review.posted_by != request.user:
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        review.delete()
        return redirect('movies')

    context = {
        'review': review,
    }
    return render(request, 'review_delete.html', context)

def loginPage(request):
    page = 'login'
    print(request.user)
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":  
        username = request.POST.get("username").lower() 
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Username or password is incorrect")
    
    context = {
        "page": page
    }

    return render(request, "login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("/")

def registerUser(request):
    form = UserCreationForm()

    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
        
            return redirect("/")
        else:
            print("Error in registration") 

    context = {
        "page_title": "Register Here",
        "form": form
    }

    return render(request, "login_register.html", context)



