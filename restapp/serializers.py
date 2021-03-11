from restapp.models import Article
from rest_framework import serializers
from django.contrib.auth.models import User


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','title','author','email','date']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']



''' 
    #normal serializer#


    title=serializers.CharField(max_length=250)
    author=serializers.CharField(max_length=200)
    email=serializers.EmailField(max_length=100)
    date=serializers.DateTimeField()

    def create(self,validated_data):
        return Article.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.author=validated_data.get('author',instance.title)
        instance.email=validated_data.get('email',instance.title)
        instance.date=validated_data.get('date',instance.title)
        instance.save()

        return instance
'''