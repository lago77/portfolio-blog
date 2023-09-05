from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
import os

import base64
import sys


class PostList(APIView):

    #@api_view(['GET'])
    def get(self, request):
        posts = Post.objects.all()
        posts1 = Post.objects.all()
        posts2= Post.objects.filter(body__startswith="te").values()
        serializer = PostSerializer(posts, many=True)
        print("*****************")
        print(posts1)
        print(posts2)
        print("******************")
        print("////////")
        for m in posts2:
            print(m)
        print("/////////////")
        print("hei hi hi hi")
        print(serializer.data)
      
        return Response(serializer.data)
    
    def post(self, request):
        print("in the post2")
        print(request.data)
        print("1")
        print(request.data['body'])
        mybody=request.data['body']
        print("2")
        print("my encoded value ")
        print(mybody)
        print("decoded value")
        convertbytes = mybody.encode("ascii")
        convertedbytes = base64.b64decode(convertbytes)
        decodedsample = convertedbytes.decode("ascii")
        print(decodedsample)
        print("-----------------")
        serializer = PostSerializer(data=request.data)
        print("my serializer2")
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
      
class PostDetail(APIView):
    def get(self, request, pk):
        mytest="test"
        mypost = Post.objects.filter(body__startswith="te")
        print("my post")
        print(mypost)
        myserializer = PostSerializer(mypost)
        print("my serializer")
        print(myserializer)
        #print(myserializer.data)
        try:
            post = Post.objects.get(pk=pk)
            #post = Post.objects.filter(body__startswith=mytest)
            print("my posting")
            print(post)
        except Post.DoesNotExist:
            return Response({'Error':'Post not found'}, status=404)
        serializer = PostSerializer(post)
        print("my data")
        print(serializer)
        print("after serializer data")
        print(serializer.data)
        return Response(serializer.data)
        
