from rest_framework import serializers

from .models import Album, TeacherModel,Track


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ['id', 'name', 'subject_teacher', 'age']

"""Relation Through StringRelatedField"""

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']

"""Nested relationships"""

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order','title','duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True , read_only = True)

    class Meta:
        model = Album
        fields = ['id','album_name','artist','tracks']