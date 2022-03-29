from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import MovieViewSet, ActorViewSet, MovieActorAPIView,CommentAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', MovieViewSet,basename='movies')
router.register('actors', ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors', MovieActorAPIView.as_view(), name='movie-actor'),
    path('comment/',CommentAPIView.as_view(),name='comment'),
    path('comment/<int:pk>/',CommentAPIView.as_view(),name='deletecomment'),
    path('auth/', obtain_auth_token, name='auth'),

]
