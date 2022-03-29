from django.db import models


class Actor(models.Model):
    GENDER_CHOICE = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICE)
    birthdate = models.DateField()

    class Meta:
        db_table = "Actor"
