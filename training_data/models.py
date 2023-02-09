from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=75)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class News(models.Model):
    class Sentiment(models.TextChoices):
        POSITIVE = ('positive', 'positive')
        NEUTRAL = ('neutral', 'neutral')
        NEGATIVE = ('negative', 'negative')

    url = models.URLField()
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=750,
                                   blank=True,
                                   null=True)
    sentiment = models.CharField(max_length=15, 
                                 blank=True,
                                 null=True,
                                 choices=Sentiment.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
