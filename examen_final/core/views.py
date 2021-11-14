from re import template
from django.db.models import fields
from django.db.models.fields import CharField
from django.forms import forms
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, EditForm, SignUpForm,  EditProfileForm
from examen_final.core import models
from .models import Post, Category, Profile
from django.http import HttpResponseRedirect
from slick_reporting.views import SlickReportView









def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomeView')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


class HomeView (ListView):
    model = models.Post
    template_name = 'HomeView.html'
    ordering =['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
        



class ArticleDetailView(DetailView):
    model = models.Post
    template_name = 'article-details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)


        stuff = get_object_or_404(Post, id=self.kwargs['pk']) #captura el post, dependiendo de cual es su id
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context



class AddPostView(CreateView):
    model = models.Post
    form_class = PostForm
    template_name = 'add_post.html'

    
    #Agregamos los fields
    #fields = ('title','author','body' ) ya no lo usamos porque ahora usamos el forms.py

class UpdatePostView(UpdateView):
    model = models.Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'author', 'body']

class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('HomeView')

class AddCategoryView(CreateView):
    model = models.Category
    template_name = 'add_category.html'
    fields = '__all__'



def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-',' '), 'category_posts': category_post})


def CategoryListView(request):
    cat_menu_list = Category.objects.all
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('HomeView')

    def get_object(self):
        return self.request.user

class ShowProfilePageView(DetailView):
    model = models.Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
       # users = Profile.objects.all()
        context = super( ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context['page_user'] = page_user
        return context
        
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'fb_url', 'instagram_url']

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile_page.html'
    fields = ['bio', 'profile_pic', 'fb_url', 'instagram_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class SimpleListReport(SlickReportView):
    
    report_model = models.Post
    # the model containing the data we want to analyze

    date_field = 'post_date'
    # a date/datetime field on the report model

    # fields on the report model ... surprise !
    columns = ['title', 'post_date', 'category', 'likes']




