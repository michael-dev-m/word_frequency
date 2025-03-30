from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    word = models.CharField(max_length=25, unique=True)
    count = models.IntegerField()
    users = models.ManyToManyField(User, through='Check')

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['count']
        indexes = [
            models.Index(fields=['word']),
        ]


class Check(models.Model):

    class Status(models.TextChoices):
        FAMILIAR = 'FM', 'FAMILIAR'
        UNFAMILIAR = 'UF', 'UNFAMILIAR'
        UNSORTED = 'US', 'UNSORTED'

    user = models.ManyToManyField(User, on_delete=models.CASCADE)
    word = models.ManyToManyField(Card, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(choices=Status.choices,
                              max_length=2,
                              default=Status.UNSORTED)


class PartOfText(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    words = models.ManyToManyField(Card)

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_texts')

    def __str__(self):
        return self.title




