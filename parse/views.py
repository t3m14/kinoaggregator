from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .parse import parse_impulse

class MyOwnView(APIView):
    def get(self, request):
        return Response(parse_impulse())