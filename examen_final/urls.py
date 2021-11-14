from re import template
from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
from django.contrib.auth import views as auth_views
from examen_final.core import views
from django.conf import settings
from django.conf.urls.static import static

from examen_final.settings import MEDIA_URL

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/password_change_form.html')),
    path('HomeView/', views.HomeView.as_view(), name='HomeView'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-details'),
    path('addpost/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remover', views.DeletePostView.as_view(), name='delete_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),
    # path('article/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('report/', views.SimpleListReport.as_view(), name = 'report'),
    
    

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
