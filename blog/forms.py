from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
    desc = forms.CharField(widget= forms.Textarea(), max_length=5000, required=True, help_text="description doo")

    class Meta:
        model = Post
        fields = ['author', 'title','desc', 'img', ]


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=40, 
        required=True, 
        help_text="Enter a unique username that contains only letters, digits and @/./+/-/_ characters"
    )
    class Meta:
        model = User
        fields = [ 'username', 'password1' ,'password2']
        
