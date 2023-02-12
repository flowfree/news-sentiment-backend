from lxml import etree
import requests 

from .exceptions import ScraperError 


def get_metadata_from_url(url: str) -> dict:
    meta = {
        'url': url,
        'title': '',
        'description': '',
        'image_url': '',
    }

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise ScraperError(e)
    
    tree = etree.HTML(r.text)
    
    try:
        elem = tree.xpath('//head/title')
        meta['title'] = elem[0].text.strip()
    except Exception: 
        raise ScraperError('Failed extracting metadata')

    try:
        elem = tree.xpath('//head/meta[@name="description"]')
        meta['description'] = elem[0].attrib['content']
    except Exception: 
        pass

    try:
        elem = tree.xpath('//head/meta[@property="og:image"]')
        meta['image_url'] = elem[0].attrib['content']
    except Exception: 
        pass

    return meta
