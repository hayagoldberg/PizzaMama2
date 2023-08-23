from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('make-an-order/', views.order_view, name='order'),
    path('menu/', views.menu_view, name='menu'),
    path('index', views.index_view, name='index'),
]
