# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from webapp.models import employees
from .serializers import employeesSerializer
# Create your views here.

class employeeList(APIView):

    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1, many=True)
        return Response(serializer.data)


    def post(self):
        pass
