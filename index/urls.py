from . import views
from django.urls import path
from .views import  SearchResultsView,FoodApiDetail
urlpatterns = [

#App Urls
	#path('mobile/', MobileRedirect.as_view(), name='mobile_redirect'),
	path('search/', SearchResultsView.as_view(), name='search_results'),
    path('recipe/', views.RecipeList.as_view(), name='RecipeList'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('', views.FoodsList.as_view(), name='home'),

]