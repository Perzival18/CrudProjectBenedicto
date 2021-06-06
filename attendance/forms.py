from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'year', 'course', 'email', 'contact', 'date']
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'year': forms.TextInput(attrs={ 'class': 'form-control' }),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),

    }