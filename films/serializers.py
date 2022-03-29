from rest_framework import serializers
from films.models import Actor, Movie, Comment
from rest_framework.exceptions import ValidationError



class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id']

    def validate_birthdate(self, value):
        if value.year<1950:
            raise ValidationError("This is not true")
        elif value.year==1950 and value.month==1 and value.day==1:
            raise ValidationError("This is not true")

        return value



class MovieSerializer(serializers.ModelSerializer):
    # actor = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','movie_id','text','created_date')