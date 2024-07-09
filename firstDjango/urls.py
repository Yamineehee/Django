# urls.py

from django.contrib import admin
from django.urls import path
from todo import views  # Ensure 'todo' is in your installed apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('Signup/', views.SignupPage, name='Signup'),
    path('Login/', views.LoginPage, name='Login'),
    path('logout/', views.logout, name='logout'),
    path('todo_list', views.todo_list, name='todo_list'),
    path('add/', views.add_item, name='add_item'),
    path('toggle/<int:item_id>/', views.toggle_item, name='toggle_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
