from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, BookInstance, Author, Genre, Language


def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_available_instances = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_language = Language.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_available_instances': num_available_instances,
        'num_authors': num_authors,
        'num_language': num_language,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.all()
    template_name = 'catalog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'


    def get_context_data(self, **kwargs):
        # Get the existing context from the parent class
        context = super().get_context_data(**kwargs)
        # Add books related to the author
        context['books'] = Book.objects.filter(author=self.object)
        return context


