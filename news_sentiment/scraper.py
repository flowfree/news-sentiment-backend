from bs4 import BeautifulSoup
import requests 

from .exceptions import ScraperError 


def get_metadata_from_url(url: str) -> dict:
    meta = {
        'url': url,
        'title': '',
        'description': '',
        'image_url': '',
        'published_time': None,
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "macOS",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise ScraperError(e)

    soup = BeautifulSoup(r.text, "html.parser")

    # Extract the meta tags
    for tag in soup.find_all('meta'):
        if tag.get('property') == 'og:title':
            meta['title'] = tag.get('content')
        if tag.get('property') == 'og:description':
            meta['description'] = tag.get('content')
        elif tag.get('property') == 'og:image':
            meta['image_url'] = tag.get('content')
        elif tag.get('property') == 'article:published_time':
            meta['published_time'] = tag.get('content')

    return meta
