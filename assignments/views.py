from multiprocessing import managers
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from assignments.models import assignments
from assignments.serializeers import AssignmentSerializer
from django.http import HttpResponse
import random
import string

# Create your views here.


@api_view(['GET'])
def view_task(request):

    assignments_objects = assignments.objects.all()
    serializer = AssignmentSerializer(assignments_objects, many = True)
    # return HttpResponse(generate_id())
    # print(serializer.data.items)
    return Response(serializer.data)


@api_view(['POST'])
def new_task(request):

    assignments_objects = assignments.objects.all()
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    # return HttpResponse(generate_id())
    # print(serializer.data.items)

