from django import forms
from polls1.models import Book, Read


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class ReadForm(forms.ModelForm):
    class Meta:
        model = Read
        fields = ['content']
        labels = {
            'content': '후기',
        }