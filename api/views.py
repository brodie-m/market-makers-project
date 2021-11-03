from django.shortcuts import render
from rest_framework import generics
from .serializers import ETFSerializer
from .models import ETF


class ETFView(generics.ListAPIView):
    queryset = ETF.objects.all()
    serializer_class = ETFSerializer
