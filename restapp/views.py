from django.shortcuts import render
from restapp.models import Article
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapp.serializers import ArticleSerializers,UserSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics,viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,BasePermission,SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


# Create your views here.

class ArticleList(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializers
    
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated|ReadOnly]



class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializers
    
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated|ReadOnly]


#viewsets with routers
class UserList(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    


#viewsets with routers
class UserDetails(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    










# Generic Article View

class GenericArticleview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializers
    lookup_field='id'
    
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request):
        return self.destroy(request)
        

#Viewsets article view
class ViewSetArticleView(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializers






'''
# Class Based api views

class ArticleList(APIView):
    def get(self,request, format=None):
        articles=Article.objects.all()
        serializer=ArticleSerializers(articles,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer=ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self,pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self,request,pk,fomat=None):
        article=self.get_object(pk)
        serializer=ArticleSerializers(article)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        article=self.get_object(pk)
        serializer=ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        article=self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''





















       
       
'''     
       #Fuction Based Api Views



# see the api list and post methods code for Article model
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles=Article.objects.all()
        serializer=ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer=ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update or delete a code of Article model

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=ArticleSerializers(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






'''

    