from . import views
from django.urls import path
from .views import  SearchResultsView
urlpatterns = [
	path('search/', SearchResultsView.as_view(), name='search_results'),

    path('', views.FoodsList.as_view(), name='home'),
    path('recipe/', views.RecipeList.as_view(), name='RecipeList'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]