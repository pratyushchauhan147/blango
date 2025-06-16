from django.urls import path,include,re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from blog.api.views import PostList, PostDetail,UserDetail


urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)