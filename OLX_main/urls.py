from django.urls import path
from .import views


urlpatterns = [
    path('', views.ProductView.as_view(), name='main'),
    path('datail/<slug:slug>', views.ProductDatailView.as_view(), name='datail'),
    path('search/', views.SearchView.as_view(), name='search')
]
