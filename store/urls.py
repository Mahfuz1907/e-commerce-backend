from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('categories/', views.CategoryListAPI.as_view(), name='category_list_api'),
    path('products/', views.ProductListAPI.as_view(), name='product_list_api'), 
    path('product/<int:product_ID>/', views.ProductDetailsAPI.as_view(), name='product_api'),
    path('products/<int:category_id>/', views.ProductByCategory.as_view(), name='product_by_category_api'), 
    path('products/search/', views.ProductSearchAPI.as_view(), name='product_search_api'),
]