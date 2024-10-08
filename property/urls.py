from django.urls import path
from property import views

urlpatterns = [
    path('property/', views.PropertyView.as_view(), name='Property'),
    path('property/<int:pk>/', views.PropertyViewRetriveUpdateDestroyDetail.as_view(), name='Property')
]