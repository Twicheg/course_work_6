from django.urls import path

from users.apps import UsersConfig
from users.views import LIView, LOView, RegisterView, verification, genpass, UserUpdateView, UserListView, \
    UserDeleteView, user_deactivate, user_activate

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LIView.as_view(), name='login'),
    path('logout/', LOView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/<int:pk>/', verification, name='verification'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('update/genpass', genpass, name='genpass'),
    path('users/list', UserListView.as_view(), name='list'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),
    path('deactivate/<int:pk>/', user_deactivate, name='deactivate'),
    path('activate/<int:pk>/', user_activate, name='activate'),

]
