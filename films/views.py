from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieSerializer, ActorSerializer, CommentSerializer
from films.models import Movie, Actor, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    filter_fields = ['genre']
    search_fields = ['name']
    ordering_fields = ['imdb','-imdb']
    # ordering = ['-imdb']


    @action(detail=True, methods=["POST"], url_path='add-actor')
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["id"]
        actor = Actor.objects.get(pk=actor_id)
        movie.actor.add(actor)
        movie.save()
        return Response({'status': 'success'})

    @action(detail=True, methods=["DELETE"], url_path='remove-actor')
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["id"]
        actor_d = Actor.objects.get(pk=actor_id)
        movie.actor.remove(actor_d)
        movie.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class MovieActorAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        serializer = ActorSerializer(movie.actor.all(), many=True)

        return Response(data=serializer.data)


class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self,request):
        comments = Comment.objects.filter(user_id=self.request.user)
        serializer = CommentSerializer(comments,many=True)
        return Response(data=serializer.data)
    def post(self,request):
        serializer = CommentSerializer(data = request.data)
        # request.data['user_id'] = request.user
        serializer.is_valid(raise_exception=True)

        serializer.save(user_id=request.user)
        return Response(data = serializer.data)

    def delete(self,request,pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class MovieAPIView(APIView):
#     def get(self,request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(data=serializer.data)
#     def post(self,request):
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie = serializer.save()
#         return Response(data=serializer.data)
# class ActorAPIView(APIView):
#     def get(self,request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(data=serializer.data)
#
#     def post(self,request):
#         serializer = ActorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         actor = serializer.save()
#         return Response(data=serializer.data)
