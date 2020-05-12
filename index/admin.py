from django.contrib import admin
from .models import Foods, Recipe
from import_export.admin import ImportExportModelAdmin

 

class FoodsAdmin(ImportExportModelAdmin):
    list_display = ('title',  'gi','serve','carb_per_serve','gl')
    list_filter = ("title",)
    search_fields = ['title', ]

class RecipeAdmin(ImportExportModelAdmin):
    list_display = ('title', 'slug','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Foods,FoodsAdmin)
admin.site.register(Recipe,RecipeAdmin)
