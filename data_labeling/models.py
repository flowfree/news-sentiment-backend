from urllib.parse import urlsplit 
import re

from django.db import models

from . import scraper
from .exceptions import ScraperError


class Site(models.Model):
    name = models.CharField(max_length=75)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    class Sentiment(models.TextChoices):
        POSITIVE = ('positive', 'positive')
        NEUTRAL = ('neutral', 'neutral')
        NEGATIVE = ('negative', 'negative')

    url = models.URLField(unique=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=750, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    sentiment = models.CharField(max_length=15, 
                                 blank=True,
                                 null=True,
                                 choices=Sentiment.choices)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    published_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.title and not self.description:
            self.site = self._get_site(self.url)

            meta = scraper.get_metadata_from_url(self.url)
            self.title = meta.get('title', '')
            self.description = meta.get('description', '')
            self.image_url = meta.get('image_url', '')
            self.published_time = meta.get('published_time')

            self.title = self._cleanup_title(self.title)

        return super().save(*args, **kwargs)

    def _get_site(self, url: str) -> Site:
        parsed_url = urlsplit(url)
        site_url = f'{parsed_url.scheme}://{parsed_url.hostname}'
        try:
            return Site.objects.get(url__startswith=site_url)
        except Site.DoesNotExist:
            raise ScraperError(f'{parsed_url.hostname} is not supported yet.')

    def _cleanup_title(self, t: str) -> str:
        patterns = [
            '-\s+Decrypt$',
        ]
        for pattern in patterns:
            t = re.sub(pattern, '', t.strip())
        return t
