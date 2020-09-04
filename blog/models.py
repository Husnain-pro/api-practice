from django.db import models


class TeacherModel(models.Model):
    name = models.CharField(max_length=15)
    subject_teacher = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True, blank=True)
    join = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-join',)

    def __str__(self):
        return self.name

class Album(models.Model):
    album_name = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)

    
    def __str__(self):
        return self.album_name


class Track(models.Model):
    album = models.ForeignKey(Album,related_name='tracks',on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length = 100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album','order']
        ordering = ['order']

        def __str__(self):
                return f'{self.order} , {self.title}'