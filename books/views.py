from django.shortcuts import render, get_object_or_404, redirect
from django.template import context
from books.models import Book, Review
from django.views.generic import ListView, DetailView

from django.core.files.storage import FileSystemStorage
from books.forms import ReviewForm

# we create a new class where we list all books that will replace the index definition
class BookListView(ListView):
       
    def get_queryset(self):
        return Book.objects.all()
    

class BookDetailView(DetailView):
    model = Book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all() # we fetch all the authors and create the context
        context['form'] = ReviewForm()
        return context
    
def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books} 
    return render(request, 'books/book_list.html', context)

def review(request, id):
    if request.user.is_authenticated :
        newReview = Review(book_id=id, user=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=newReview)
        if form.is_valid():
            form.save()
    return redirect(f"/{id}")
    


    
