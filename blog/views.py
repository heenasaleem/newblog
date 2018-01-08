from django.shortcuts import render
from . models import BlogList
from django.template import loader
from django.http import HttpResponseRedirect
from .form import BlogForm 
from .form import SignUpForm
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages




# Create your views here.

def index(request):
    latest_blog_list = BlogList.objects.order_by('-pub_date')[:5]
   # template = loader.get_template('polls/index.html')
    context = {
        'latest_blog_list': latest_blog_list,
    }
    return render(request, 'blog/index.html', context)


def save_data(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
           # blog.published_date = timezone.now()
            blog.save()
            return HttpResponseRedirect(reverse('blog:index'))
            #return redirect('post_detail', pk=blog.pk)
            #return HttpResponseRedirect(reverse('blog:post_detail', pk=pk))
    else:
        form = BlogForm()
        print('inside else')

    return render(request, 'blog/index2.html', {'form': form})

def edit_blog(request, id=None):
    item = get_object_or_404(BlogList,id=id)
    print("item is :", item)
    form = BlogForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('blog:index'))
#return render(request, 'blog/index2.html', {'form': form})

def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', pk)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("after post...")
        user = authenticate(request, username=username, password=password)
        print("after post 2..")
        if user is not None:
            print("inside if")
            login(request, user)
        return HttpResponseRedirect(reverse('blog:index'))

    else:
        return render(request, 'blog/login.html')

def signup(request):
    print("problem 1")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("form is:", form)
        if not form.is_valid():
            print("problem")
            messages.add_message(request, messages.ERROR,'There is problem')
            return render(request, 'blog/signup.html', {'form': form})
        else:
            username =form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username, email, password)
            #user = authenticate(username=username, password=password)
            #login(request, user)
            messages.add_message(request, messages.SUCCESS, 'ACCOUNT CREATED')
            return HttpResponseRedirect(reverse('blog:signin'))
    else:
        return render(request, 'blog/signup.html',{'form': SignUpForm() })




def delete_blog(request, id=None):
    item = get_object_or_404(BlogList,id=id)
    print("item is:", item)
    form = BlogForm(request.POST or None, instance=item)
    print("form is:", form)
    #if form.is_valid():
    print("true")
    item.delete()
        
    return HttpResponseRedirect(reverse('blog:index'))

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:signin'))
    
    
    
            

