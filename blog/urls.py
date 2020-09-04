from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('teacher_api/', views.TeacherListView.as_view(),name='teacher_list'),
    path('teacher_api/<pk>', views.TeacherDetailView.as_view(),name='teacher_list_detail'),
    path('album_api/', views.AlbumView.as_view(),name='album'),
    path('album_api/<pk>', views.AlbumViewDetail.as_view(),name='album_detail'),

]