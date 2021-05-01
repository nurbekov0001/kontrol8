from django.urls import path

from webapp.views.product import (
    ProductList,
    ProductCreate,
    ProductDeleteView,
    ProductUpdateView,
    ProductView
)

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<int:pk>/', ProductView.as_view(), name='view'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('project/add/', ProductCreate.as_view(), name='add')]