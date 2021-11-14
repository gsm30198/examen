from django import forms
from django.forms import fields, widgets
from .models import  Post, Category
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User



choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category','resumen','body', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe aquí'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}),
            'resumen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Haz una breve descripción'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu post aquí'}),
            
        
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','resumen', 'category' ,'body', 'header_image' )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe aquí'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}),
            'resumen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Haz una breve descripción'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu post aquí'}),
            
            
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    # last_login = forms.CharField(max_length=100)
    # is_superuser = forms.CharField(max_length=100)
    # is_staff = forms.CharField(max_length=100)
    # is_active= forms.CharField(max_length=100)
    # date_joined = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name','body')
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe aquí'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu post aquí'}),
            
#         }








