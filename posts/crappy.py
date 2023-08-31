from rest_framework import generics, request, viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    print("hello world")
    print("Hey there2")
    def get(self, request):
        print("testing 123")
        print(request)
        return Response
    #     print(serializer_class.data)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Post.objects.all()
        print("hello world")
        print(request)
        serializer_class = PostSerializer

        