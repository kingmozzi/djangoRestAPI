import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .api import PracticeSerializer
from .models import Practice
from rest_framework.parsers import JSONParser

# class PracticeViewSet(viewsets.ModelViewSet):
#     queryset = Practice.objects.all()
#     serializer_class = PracticeSerializer
#     permissions_class = [permissions.IsAuthenticated]

@csrf_exempt
def practice_list(request):
    if request.method == 'GET':
        queryset = Practice.objects.all()
        serializer = PracticeSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PracticeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def practice(request, id):
    obj = Practice.objects.get(id=id)

    if request.method == 'GET':
        serializer = PracticeSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PracticeSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_name = data['name']
        obj = Practice.objects.get(name=search_name)

        if data['uid'] == obj.uid:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)