from django import forms
from.models import profile
from django.contrib.auth.models import User
class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم',max_length=100, help_text='يجب الا يحتوى الاسم على مسافات ')
    email = forms.EmailField(label='البريد الالكترونى')
    first_name = forms.CharField(label='الاسم الأول ',max_length=100)
    last_name = forms.CharField(label='الاسم الأخير',max_length=100)
    password1 = forms.CharField(label='كلمه المرور',min_length=8,max_length=20,widget=forms.PasswordInput(),help_text='يجب الا تقل كلمه المرور عن 8 احرف')
    password2 = forms.CharField(label='تأكيد كلمه المرور',min_length=8,max_length=20,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1','password2')
    #to amke sure that password1 is equal to password2
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise forms.ValidationError('كلمه المرور غير متطابقه!!')
        return cd['password2']
    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('اسم المستخدم موجود بالفعل جرب اسم اخر ')
        return cd['username']

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم',max_length=100)
    password = forms.CharField(label='كلمه المرور',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم',max_length=100)
    password = forms.CharField(label='كلمه المرور',widget=forms.PasswordInput())
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label='البريد الإلكتروني')

    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name', 'email')
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('image',)

