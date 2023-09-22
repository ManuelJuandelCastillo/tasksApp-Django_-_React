from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls))
]
