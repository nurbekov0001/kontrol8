from django.urls import path

from webapp.views import (
    ProductList,
    ProductCreate,
    ProductDeleteView,
    ProductUpdateView,
    ProductView,
    ReviewDeleteView,
    ReviewUpdateView,
    ReviewCreate,

)

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<int:pk>/', ProductView.as_view(), name='view'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),

    path('project/add/', ProductCreate.as_view(), name='add'),
    path('review/<int:pk>/add/', ReviewCreate.as_view(), name='review_add'),

    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),


]