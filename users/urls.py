from django.urls import path

from users.apps import UsersConfig
from users.views import LIView, LOView, RegisterView, verification, genpass, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LIView.as_view(), name='login'),
    path('logout/', LOView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/<int:pk>/', verification, name='verification'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('update/genpass', genpass, name='genpass'),
]
