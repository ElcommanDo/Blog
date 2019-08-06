from django.shortcuts import render, redirect
from .forms import UserCreationForm,LoginForm,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from Blog.models import post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage

# Create your views here.
def register(request):

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()


            username = form.cleaned_data['username']
            messages.success(request,'تهانينا{}لقد تم التسجيل بنجاح '.format(username))
            return redirect('login')

           # messages.success(request,f'تهانينا {username}لقد تم التسجل بنجاح ')



    else:
        form = UserCreationForm()

    return render(request,'user/register.html',{'title':'التسجيل','form':form})
def login_user(request):
    if request.method =='POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.warning(request,'اسم المستخدم او كلمه المرور خطأ ')
    else:
        form = LoginForm()
    return render(request,'user/login.html',{'title':'تسجيل الدخول ','form':form})
def logout_user(request):
    logout(request)
    return render(request,'user/logout.html',{})
#to make sure that user is logged in and redirect him to login page by login_url
@login_required(login_url='login')
def profile(request):

    posts = post.objects.filter(author=request.user)
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_page)

    return render(request,'user/profile.html',{'posts':posts,'posts_list':posts_list,'page': page})
@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_update = user_form.save(commit=False)
            user_update.set_password(user_form.cleaned_data['password'])
            user_update.save()
            profile_form.save()

            messages.success(
                request, 'تم تحديث الملف الشخصي.')
            return redirect('profile')
    else:
         user_form = UserUpdateForm(instance=request.user)
         profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(
        request, 'user/profile_update.html',
                 {'user_form': user_form,
                 'profile_form': profile_form})



