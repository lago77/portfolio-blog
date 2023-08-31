from django.urls import path
from .views import PostList
from .views import PostDetail
urlpatterns = [
path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
path("", PostList.as_view(), name="post_list"),
path("post", PostList.as_view(), name="post_make"),
#path("do", DoSomething.as_view(), name="post_do"),
]