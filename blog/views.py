from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def feed(request):

    myobjects = Post.objects.all()
    param = {
        'object':myobjects
    }
    return render(request, 'blog/home.html', param)
    # return HttpResponse('HI there')
def adminFeed(request):
    myobjects = Post.objects.all()
    param = {
        'object':myobjects
    }
    return render(request, 'blog/adminHome.html', param)

def post(request, id):
    if request.method == 'GET':
        myobj = Post.objects.get(id=id)
        param = {
        'object': myobj
        }
        return render(request, 'blog/post.html', param)


def addPost(request):
    if request.method == "POST":
        fm = PostForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        print(fm)
    else:
        fm = PostForm()
    return render(request,'blog/create.html' , {'form':fm} )

def upPost(request, id):
    if request.method == 'POST':
        blog = Post.objects.get(id=id)
        fm = PostForm(request.POST, request.FILES, instance=blog)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        print(request)
        blog = Post.objects.get(id=id)
        fm = PostForm(instance=blog)
    return render(request, 'blog/update.html', {'form':fm})

def admin_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data= request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            password = fm.cleaned_data.get('password')
            user = authenticate(request, username=username, password= password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        fm = AuthenticationForm()
    return render(request, 'blog/login.html', {'form':fm})


def admin_logout(request):
    logout(request)
    return redirect('/login')


def register(request):
    if request.method =='POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            username = fm.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        fm = UserCreationForm()
    return render(request, 'blog/register.html', {'form': fm})


def deletePost(request, id):
    blog = Post.objects.get(id=id)
    blog.delete()
    return redirect('/')
    