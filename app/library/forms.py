from .models import Library, Book
from django.forms import ModelForm, TextInput, HiddenInput

class LibraryForm(ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'picture']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название библиотеки'
            }),
            'picture': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте URL изображения'
            }),
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте автора'
            }),
            'library': HiddenInput(),
        }