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
