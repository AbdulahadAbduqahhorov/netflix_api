from django.test import TestCase,Client
from django.urls import reverse
from films.models import Movie
from films.serializers import MovieSerializer


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        Movie.objects.create(name='Spider man',year='2001-02-03',imdb=8,genre='fantastic')
        Movie.objects.create(name='Avengers 2',year='2004-03-04',imdb=7,genre='fantastic')
        Movie.objects.create(name='Iron man 3',year='2007-04-01',imdb=9,genre='fantastic')
        self.client = Client()

    def test_get_all_movie(self):
        response = self.client.get(reverse('movies-list'))
        movies = Movie.objects.all()
        serializer =MovieSerializer(movies,many=True)
        self.assertEquals(response.data,serializer.data)
        self.assertEquals(response.status_code,200)

    def test_movie_search(self):
        response = self.client.get('/movies/?search=Spider')
        data =response.data

        self.assertEquals(response.status_code,200)
        self.assertEquals(len(data),1)
        self.assertEquals(data[0]['name'],"Spider man")

    def test_ordering_imdb(self):
        response = self.client.get('/movies/?ordering=imdb')
        data = response.data

        self.assertEquals(response.status_code,200)
        self.assertEquals(data[0]['imdb'],7)

