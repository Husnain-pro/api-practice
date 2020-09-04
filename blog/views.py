from rest_framework import generics, mixins

from .models import TeacherModel
from .serializers import TeacherSerializer


class TeacherListView(generics.ListCreateAPIView):

    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer


