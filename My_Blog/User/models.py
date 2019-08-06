from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
# Create your models here.
class profile(models.Model):
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return '{} profile'.format(self.user.username)
    #this function to make image with less resolution to save time and space in db
    def save(self,*args,**kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 300 or img.height >300 :
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.image.path)
#this function to make profile added to adminstration dashboared
#we there used  signals post_save
def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile = profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

