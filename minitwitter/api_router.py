from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from user import urls as users_urls
from posts import urls as posts_urls
from user.serializer import MyTokenObtainPairView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

api_urlpatterns = [
    path('users/', include(users_urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair', ),
    path('posts/', include(posts_urls))
    

]

app_name = "api"
urlpatterns = router.urls
urlpatterns += api_urlpatterns