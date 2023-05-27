from django.urls import path
from .views import PostViewSet

app_name = 'posts'

urlpatterns = [
    path('', PostViewSet.as_view({'get':'list', 'post': 'create'}), name='posts')
] 