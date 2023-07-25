from rest_framework import generics
from .serializer import EggsSerializer
from .models import Eggs


class EggsList(generics.ListCreateAPIView):
    queryset = Eggs.objects.all()
    serializer_class = EggsSerializer


class EggsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eggs.objects.all()
    serializer_class = EggsSerializer

# Create your views here.
