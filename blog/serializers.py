from rest_framework import serializers

from .models import TeacherModel


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ['id','name','subject_teacher','age']
    
