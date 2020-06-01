from django.urls import path
from . import views

urlpatterns = [
    path('google', views.GoogleLoginView.as_view(), name='gooogle_login'),
    path('facebook', views.FacebookLogin.as_view(), name='facebook_login'),
    path('github', views.GithubLogin.as_view(), name='githubb_login')
]
