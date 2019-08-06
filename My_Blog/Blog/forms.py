from django import forms
from .models import comment,post
class NewComment(forms.ModelForm):
    class Meta:
       model = comment
       fields = ('name','email','body')

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينه')
    content = forms.CharField(label='نص التدوينه',widget=forms.Textarea)
    class Meta:
        model = post
        fields = ('title','content')

