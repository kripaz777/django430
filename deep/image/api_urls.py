from django.urls import path, include
from rest_framework import routers
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('image-demo',  DemoViewSet.as_view(), name='image-demo'),
    path('image-predict',  PredictViewSet.as_view(), name='image-predict'),
    path('model-crud/<int:pk>',MyModelCRUDViewSet.as_view(), name='model-crud'),
]