from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.details_page, name='details_page'),
        path('edit/', views.edit_page, name='edit_page'),
        path('delete/', views.delete_page, name='delete_page'),
    ])),
]
