from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView,
    HomePageView
)

urlpatterns = [
    path("products/<int:pk>/", ProductDetailView.as_view(),
        name="product_detail"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(),
        name="product_edit"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(),
        name="product_delete"),
    path("products/new/", ProductCreateView.as_view(), name="product_new"),
    path("products", ProductListView.as_view(), name="product_list"),
    path("", HomePageView.as_view(), name="home"),
]
