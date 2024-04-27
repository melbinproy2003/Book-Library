from django import forms
from .models import Book,Author

class AuthorForm(forms.ModelForm):
          class Meta:
                    model = Author
                    fields = ['name']
                    widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of author'})
                    }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'select author'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'})
        }