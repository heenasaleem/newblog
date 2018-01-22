from django.shortcuts import render
from . models import BlogList
from django.template import loader
from django.http import HttpResponseRedirect
from .form import BlogForm 
from .form import SignUpForm
from .form import LoginForm
from .form import UpdateProfile
from .form import UploadFileForm
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from tablib import Dataset
import xlrd
from django.http import HttpResponse
import xlwt



# Create your views here.

def index(request):
    #latest_blog_list = BlogList.objects.order_by('-pub_date')[:5]
    latest_blog_list = BlogList.objects.filter(user=request.user).order_by('-pub_date')

   # template = loader.get_template('polls/index.html')
    context = {
        'latest_blog_list': latest_blog_list,
    }
    return render(request, 'blog/index.html', context)


def save_data(request):
    if request.method == 'POST':
        user = BlogList(user=request.user)
        form = BlogForm(request.POST, instance=user)
        if form.is_valid():
            blog = form.save(commit=False)
           # blog.published_date = timezone.now()
            blog.save()
            return HttpResponseRedirect(reverse('blog:index'))
            #return redirect('post_detail', pk=blog.pk)
            #return HttpResponseRedirect(reverse('blog:post_detail', pk=pk))
    else:
        form = BlogForm()
        print('inside save_data else')

    return render(request, 'blog/index2.html', {'form': form})

def edit_blog(request, id=None):
    item = get_object_or_404(BlogList,id=id)
    print("item is :", item)
    form = BlogForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
    #return HttpResponseRedirect(reverse('blog:index'))
    return render(request, 'blog/index2.html', {'form': form})

def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', pk)

def signin(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        '''
        username = request.POST['username']
        password = request.POST['password']
        print("after post...")
        user = authenticate(request, username=username, password=password)
        print("user is:",user)
        '''
        if user:
            print("inside if")
            print(form.errors)
            login(request, user)
            #return HttpResponseRedirect(reverse('blog:index'))
            return HttpResponseRedirect(reverse('blog:save_data'))
        else:
            print("error")
            print(form.errors)
    else:
        return render(request, 'blog/login.html', {'form':form })

def signup(request):
    print("problem 1")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("form is:", form)
        if not form.is_valid():
            print("form errors",form.errors)
            print("problem")
            messages.add_message(request, messages.ERROR,'There is problem')
            return render(request, 'blog/signup.html', {'form': form})
        else:
            username =form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            args = { 'password':form['password'], 'email':form['email']}
        
            #User.objects.create_user(username, email, first_name, last_name, password)
            User.objects.create_user(**{'username': username, 'first_name': first_name, 'last_name':last_name, 'password':password, 'email':email})
           # User.objects.create_user(username=['username'], first_name=form['first_name'], last_name=form['last_name'], password=form['password'], email=form['email'],)
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
    
    
def reset(request):
    return password_reset(request, template_name='blog/reset.html',
                         email_template_name='auth/reset_email.html',
                         subject_template_name='auth/reset_subject.txt',
                         post_reset_redirect='blog/login.html')


def change_password(request):
    if request.method == 'POST':
        print("post")
        form = PasswordChangeForm(user=request.user, data=request.POST)
        print(dir(form))
        if form.is_valid():
            print("inside if2")
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your passwordwas successfully updated')
            #return redirect('change_password')
            return render(request, 'blog/login.html')
        else:
            print("incorrect")
            print(form.errors)
            messages.error(request,'Please correct the error below.')
    else:
        form =PasswordChangeForm(request.user)
    return render(request, 'blog/change_password.html', { 'form': form})

def profile(request):
    return render(request, 'blog/profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

        return render(request, 'blog/profile.html', {'form': form})
    else:
        form = UpdateProfile(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        print("upload")
        print(request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        print("form is",form)
        if form.is_valid():
            print("form is valid")
            handle_uploaded_file(request, request.FILES['file'])         

            return HttpResponseRedirect(reverse('blog:index'))

    else:
        form = UploadFileForm()
    return render(request, 'blog/upload.html', {'form': form})

def handle_uploaded_file(request,f):
    print("inside handle_uploaded_file")
    latest_blog_list = BlogList.objects.filter(user=request.user)
    print("user_blogs:", latest_blog_list)
    blog_data = xlrd.open_workbook(file_contents=f.read())
    print("blog is:", blog_data)
    for sheet in blog_data.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols
        print("rows and cols:",number_of_rows,number_of_columns)

        for row in range(1, number_of_rows):
            blog_title = (sheet.cell(row, 0).value)
            blog_body = (sheet.cell(row, 1).value)
            print("title, blog:xls data:", blog_title, blog_body)
            for item in latest_blog_list:
                title_in_db = item.title
                blog_in_db = item.body
                print("db content:", title_in_db, blog_in_db)

                if blog_title == title_in_db and blog_body != blog_in_db:
                    print("not same")
                    print("title",blog_title, title_in_db)
                    print("blog & db1:",blog_body, blog_in_db)
                    BlogList.objects.filter(title=title_in_db, user=request.user).update(body=blog_body)
               


               # elif blog_title != title_in_db and blog_body != blog_in_db:
                   # BlogList(title=blog_title,body=blog_body, user=request.user).save()
                #else:
                   # print("in else")
                   # print("blog & db3:",blog_body, blog_in_db)
                    #BlogList(title=blog_title,body=blog_body, user=request.user).save()

                '''    
                elif blog_title == title_in_db and blog_body == blog_in_db:
                    print("same blogs")
                    print("blog & db2:",blog_body, blog_in_db)
                   '''
        BlogList(title=blog_title,body=blog_body, user=request.user).save()

def download_excel_data(request):
    blogs = BlogList.objects.filter(user=request.user)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="TheDjangoBlog.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    print("wb",wb)
    ws = wb.add_sheet("sheet1")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Title','Body', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    for my_row in blogs:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.title, font_style)
        ws.write(row_num, 1, my_row.body, font_style)

    wb.save(response)
    print("res",response)
    return response

def search(request):
    #print('inside search')
    query = request.GET.get('q')
    #print("query:",query)
    latest_blog_list = BlogList.objects.filter(title__icontains=query, user=request.user).order_by('-pub_date')
    #print("blog list:", latest_blog_list)
    context = {
        'latest_blog_list': latest_blog_list,
    }
    return render(request,'blog/index.html',context)
                
            





