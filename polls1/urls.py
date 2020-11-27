from django.urls import path

from . import views

app_name = 'polls1'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('read/create/<int:book_id>/', views.read_create, name='read_create'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/modify/<int:book_id>/', views.book_modify, name='book_modify'),
    path('book/delete/<int:book_id>/', views.book_delete, name='book_delete'),
    path('read/modify/<int:read_id>/', views.read_modify, name='read_modify'),
    path('read/delete/<int:read_id>/', views.read_delete, name='read_delete'),
]
