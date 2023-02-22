from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from djangorestframework_camel_case.render import (
    CamelCaseJSONRenderer,
    CamelCaseBrowsableAPIRenderer,
)
import openai

from .scraper import get_metadata_from_url


openai.api_key = settings.OPENAI_API_KEY

if settings.DEBUG:
    renderers = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
else:
    renderers = [CamelCaseJSONRenderer]


class GetNewsSentiment(APIView):
    renderer_classes = renderers

    def get(self, request, *args, **kwargs):
        url = request.query_params.get('url')
        info = get_metadata_from_url(url)

        query = f"{info['title']} {info['description']}"
        query = query.replace('\n', ' ').strip()
        model = 'curie:ft-personal-2023-02-21-02-15-40'
        response = openai.Completion.create(
            model=model,
            prompt=f'{query}\n\n###\n\n',
            temperature=0,
            max_tokens=1,
        )
        info['sentiment'] = response['choices'][0]['text'].strip()

        return Response(info)
