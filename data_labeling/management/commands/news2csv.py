from datetime import date 
import os
import csv

from django.core.management import BaseCommand
from django.conf import settings

from ...models import News


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = []
        for news in News.objects.all():
            data.append({
                'prompt': f'{news.title}. {news.description}',
                'completion': news.sentiment
            })

        filename = settings.BASE_DIR / f'data_labeling/outputs/news-{date.today()}.csv'
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['prompt', 'completion'])
            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(f'Saved {len(data)} rows to outputs/{os.path.basename(filename)}')
