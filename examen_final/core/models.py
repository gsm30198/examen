from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.forms.fields import ImageField
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('HomeView')
   


class Post(models.Model):
    title  = models.CharField(max_length=255, verbose_name='Titulo')
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    category = models.CharField(max_length=255, default='Sin categoría', verbose_name='Categoría')
    resumen  = models.CharField(max_length=255, verbose_name='Resumen')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Autor') #aquí se usa relaciones
    body = RichTextField(blank = True, null = True)
    # body = models.TextField(verbose_name='Articulo')
    post_date = models.DateField(auto_now_add=True, verbose_name='Día posteado')
    likes = models.ManyToManyField(User, related_name='blog_post', verbose_name='Likes')

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-details', args=(str(self.id))) 
        return reverse('HomeView')

    def total_likes(self):
        return self.likes.count()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name='Biografía')
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/")
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
   

    def get_absolute_url(self):
        return reverse('HomeView')

    def __str__(self):
        return str(self.user)






















# class Comment(models.Model):
#     post =  models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE,verbose_name='Autor')
#     author = author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Autor')
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return '%s - %s' % (self.post.title, self.author)

