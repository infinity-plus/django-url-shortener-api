from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


@csrf_exempt
def shortenedURL_list(request):
    """
    List all code shortenedURLs, or create a new shortenedURL.
    """
    if request.method == 'GET':
        shortenedURLs = ShortenedURL.objects.all()
        serializer = ShortenedURLSerializer(shortenedURLs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShortenedURLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shortenedURL_detail(request, short_url):
    """
    Retrieve, update or delete a code shortenedURL.
    """
    try:
        shortenedURL = ShortenedURL.objects.get(short_url=short_url)
    except ShortenedURL.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShortenedURLSerializer(shortenedURL)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShortenedURLSerializer(shortenedURL, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shortenedURL.delete()
        return HttpResponse(status=204)


def redirect_view(request, short_url):
    """
    Redirect the short URL to link URL
    """
    if request.method == 'GET':
        try:
            shortener = ShortenedURL.objects.get(short_url=short_url)
            shortener.times_visited += 1
            shortener.save()
            return HttpResponseRedirect(shortener.long_url)
        except ShortenedURL.DoesNotExist:
            return HttpResponse(status=404)