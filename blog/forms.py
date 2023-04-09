from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput( attrs={'class': 'form-control'}))
    desc = forms.CharField(widget= forms.Textarea(attrs={'class': 'form-control'}))
    author = forms.CharField( widget= forms.TextInput(attrs={'class': 'form-control'}))
    img = forms.ImageField( widget= forms.ClearableFileInput(attrs={'class': 'form-control', 'id':'inputGroupFile02'}))

    class Meta:
        model = Post
        fields = ['author', 'title','desc', 'img']



class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=40, 
        required=True, 
        help_text="Enter a unique username"
    )
    class Meta:
        model = User
        fields = [ 'username', 'password1' ,'password2']
        # help_texts = {
        #     'username': 'Enter a unique username',
        #     'password1':'Enter Strong password' 
        # }
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }
        

