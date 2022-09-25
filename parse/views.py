from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .parse import parse_impulse, parse_comfortkino

class Impulse(APIView):
    def get(self, request):
        return Response(parse_impulse())
class Almaz(APIView):
    def get(self, request):
        return Response(parse_comfortkino("almaz"))
class Mega(APIView):
    def get(self, request):
        return Response(parse_comfortkino("mega"))
class Fokus(APIView):
    def get(self, request):
        return Response(parse_comfortkino("fokus"))
