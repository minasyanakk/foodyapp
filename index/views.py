from django.views import generic
from django.views.generic import TemplateView, ListView
from .models import Foods, Recipe
from django.db.models import Q
import operator
from rest_framework import generics
from .serializers import FoodSerializer, RecipeSerializer




#App Views
class FoodsList(generic.ListView):
    queryset = Foods.objects.order_by('title')
    template_name = 'index.html'

 

class SearchResultsView(ListView):
    model = Foods
    template_name = 'search_results.html'
    def get_queryset(self): # ne

	    query = self.request.GET.get('q')
	    if query:
	    	object_list = Foods.objects.filter(title__icontains=query)
	    	if object_list:
	    		return object_list
	    	else:
	    		self.template_name = 'retry.html'
	    else:
	    	self.template_name = 'retry.html'
	    	return self.template_name
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter().order_by('?')[:3]
    template_name = 'RecipeList.html'

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

#ApiViews
class FoodApiList(generics.ListAPIView):
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Foods.objects.all()
        food = self.request.query_params.get('q', None)
        if food is not None:
            queryset = queryset.filter(title__icontains=food)
        return queryset
    serializer_class = FoodSerializer


class FoodApiDetail(generics.RetrieveAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodSerializer




class RecipeApiList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeApiDetail(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer