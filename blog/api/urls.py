from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from blog.api.views import UserDetail, TagViewSet, PostViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns = [

    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("", include(router.urls)),
    path("posts/by-time/<str:period_name>/",PostViewSet.as_view({"get": "list"}),name="posts-by-time",),
]
