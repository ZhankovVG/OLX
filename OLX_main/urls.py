from django.urls import path
from .import views


urlpatterns = [
    path('', views.ProductView.as_view(), name='main'),
    path('create/', views.CreateProductView.as_view(), name='create_post'),
    path('datail/<slug:slug>', views.ProductDatailView.as_view(), name='datail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('comments/<int:pk>/', views.CommentsView.as_view(), name='comments'),
]
