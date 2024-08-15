from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Full name", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Full name',
        'id': 'contact-name'
    }))
    email = forms.EmailField(label="Email address", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address',
        'id': 'contact-email'
    }))
    subject = forms.CharField(max_length=50, label="Subject", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject',
        'id': 'contact-company'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'id': 'contact-message',
        'rows': 3
    }), label="Message")
