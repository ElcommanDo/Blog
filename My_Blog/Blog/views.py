from django.shortcuts import render,HttpResponse ,HttpResponseRedirect
from .models import post , comment
from .forms import NewComment,PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView
# to make pagination bar
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage

# Create your views here.
posts = [
    {'title':'التدوينه الاولى','body':'نص التدوينه الاولى كنص تجريبى ','author':'mohamed ali','date':'29-8-2019'}
    ,
    {'title':'التدوينه الثانيه','body':'نص التدوينه الثانيه كنص تجريبى ','author':'mohamed ali','date':'29-8-2019'}

    ,
    {'title':'التدوينه الثالثه','body':'نص التدوينه الثالثه كنص تجريبى ','author':'ahmed ali','date':'29-8-2019'}
 ,
     {'title':'التدوينه الرابعه','body':'نص التدوينه الرابعه كنص تجريبى ','author':'mohamed khaled','date':'29-8-2019'}

    ,
     {'title':'التدوينه الخامسه','body':'نص التدوينه الخامسه كنص تجريبى ','author':'mohamed ali','date':'29-8-2019'}

,
]
def index(request):
    posts = post.objects.all()
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)

    context = {
        'posts': posts,
        'page': page,

               }
    return render(request,'blog/index.html',context)
def about(request):
    return render(request,'blog/about.html',{})
def post_details(request,post_id):
    post1 = post.objects.get(id=post_id)
    comments =comment.objects.filter(post=post1,active=True)

    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post1
            new_comment.save()
            #Make form empty after taken request
            comment_form = NewComment()

    else:
        comment_form = NewComment()
    context = {'post':post1,'comments':comments , 'comment_form':comment_form}
    return render(request,'blog/post_detail.html',context)
class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    #fields = ['title','content']
    template_name = 'blog/new_post.html'
    form_class =PostCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = post
    template_name = 'blog/post_update.html'
    form_class =PostCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    #after that we must make post confirm delete.html to redirct to it



