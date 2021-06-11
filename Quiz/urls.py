from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#path('', views.index, name ='home'),
path('index2/', views.index2, ),
path('', views.home, name ='home'),
#path('logout/', auth_view.LogoutView.as_view(template_name ='index.html'), name ='logout'),
path('signUpView/signUp/', views.signUp, name ='signUp'),
path('signUpView/', views.signUpView, name ='signUpView'),
#path('loginView/login/', views.Login, name ='login'),
path('login/', views.Login, name="login"),
path('loginView/', views.loginView, name ='loginView'),
path('addQue/', views.addQuestion, name ='addQue'),
path('logout/', views.logoutView, name='logout'),
path('quiz/<int:id>/', views.quiz, name='quiz'),
path('report/', views.report, name='report'),
path('userProfile/', views.userProfile, name='userProfile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
