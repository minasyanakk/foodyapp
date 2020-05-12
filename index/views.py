from django.views import generic
from django.views.generic import TemplateView, ListView
from .models import Foods, Recipe
from django.db.models import Q
import operator

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