from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    movie_id = models.ForeignKey("films.Movie",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField()