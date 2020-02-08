from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Categories
from .serializer import CategoriesSerializer
from rest_framework.response import Response


class CategoriesViewSet(GenericAPIView):


    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get(self,response):

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
