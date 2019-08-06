from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_update = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # return '/detail/{}'.format(self.pk)
        return reverse('post_details', args=[self.pk])

    class Meta:
        ordering = ('-post_date',)
class comment(models.Model):
    name = models.CharField(max_length=100 ,verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الالكترونى')
    body = models.TextField(verbose_name='التعليق')
    post_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE ,related_name='comments')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-post_date',)


