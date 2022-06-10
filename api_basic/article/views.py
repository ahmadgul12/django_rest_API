
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

def article_list(request):
    if request.method=='GET':
        articles=Article.objects.all()
        Serializer=ArticleSerializer(articles,many=True)
        return JsonResponse(Serializer.data,safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        Serializer=ArticleSerializer(data=data)

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data,status=201)
        return JsonResponse(Serializer.errors,status=400)


        
        