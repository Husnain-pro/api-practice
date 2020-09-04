from rest_framework import generics, mixins
from itertools import chain

from .models import TeacherModel,Album,Track
from .serializers import TeacherSerializer,AlbumSerializer,TrackSerializer


class TeacherListView(generics.ListCreateAPIView):

    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer



class AlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

  
class AlbumViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
  