from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from hope_for_single_mothers.utils import unique_slug_generator
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    overeview = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    slug = models.SlugField(max_length=250, blank=True)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
class Signup(models.Model):
    email = models.EmailField()
    timestamp = (models.DateTimeField(auto_now_add=True))
    def __str__(self):
        return self.email


def slug_generator(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 


pre_save.connect(slug_generator, sender = Post)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return f'{self.name} {self.email}'