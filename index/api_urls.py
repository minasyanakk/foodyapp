from . import views
from django.urls import path
from .views import  SearchResultsView,FoodApiDetail
urlpatterns = [

#App Urls
	path('v1/foods/', views.FoodApiList.as_view()),
	path('v1/foods/<int:pk>/', views.FoodApiDetail.as_view()),
	path('v1/recipe/', views.RecipeApiList.as_view()),
	path('v1/recipe/<int:pk>/', views.RecipeApiDetail.as_view()),
]