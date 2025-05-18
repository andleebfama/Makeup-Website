from django.urls import path
from .views import purchase_view
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('purchase/', purchase_view, name='purchase'),
    path('category/', views.category, name='category'),
    path('category/<str:category_name>/', views.category_detail, name='category_detail'),
    path('products/', views.products_view, name='products'),
]

