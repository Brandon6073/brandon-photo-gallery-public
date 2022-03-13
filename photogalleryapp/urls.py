from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),

    path('',views.gallery, name='gallery'),
    path('photo/<str:pk>',views.photoView, name='photo'),
    
    path('add/',views.photoAdd, name='add'),
    path('update/<str:pk>',views.photoUpdate, name='update'),
    path('delete/<str:pk>', views.photoDelete, name='delete'),

]
