from django.shortcuts import render, redirect, get_object_or_404
from .models import Library, Book
from .forms import LibraryForm, BookForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.
def library_home(request):
    librarys = Library.objects.all()
    return render(request, 'library/library_home.html', {'librarys': librarys})

def createLib(request):
    error = ''
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_home')
        else:
            error = 'Форма была неверной'

    form = LibraryForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'library/createLib.html', data)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library/details.html'
    context_object_name = 'library'

class LibraryUpdateView(UpdateView):
    model = Library
    template_name = 'library/updateLib.html'

    form_class = LibraryForm

class LibraryDeleteView(DeleteView):
    model = Library
    success_url = '/library/'
    template_name = 'library/deleteLib.html'

def createBook(request, pk):
    error = ''
    library = get_object_or_404(Library, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.library = library
            book.save()
            return redirect('library-detail', pk=pk)
        else:
            error = 'Форма была неверной'
    else:
        form = BookForm(initial={'library': library.pk})

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'library/createBook.html', data)


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'library/updateBook.html'
    form_class = BookForm
    pk_url_kwarg = 'book_id'

    def get_success_url(self):
        pk = self.kwargs['pk']
        book_id = self.kwargs['book_id']

        return reverse_lazy('library-detail', kwargs={'pk': pk})

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/deleteBook.html'
    pk_url_kwarg = 'book_id'

    def get_success_url(self):
        library_id = self.kwargs['library_id']
        return reverse_lazy('library-detail', kwargs={'pk': library_id})