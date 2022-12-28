from django.db import models


class Place(models.Model):
    name=models.TextField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    member=models.CharField(max_length=150)
    picture = models.ImageField(upload_to='pics')
    decription = models.TextField()

    def __str__(self):
        return self.member





