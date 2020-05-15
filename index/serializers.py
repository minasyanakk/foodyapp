from rest_framework import serializers
from . import models


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title','gi')
        model = models.Foods


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title','content')
        model = models.Recipe

