from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, FetchAndUpdateCityData

router = DefaultRouter()
router.register(r'items', ItemViewSet)


urlpatterns = [
    path('city-info', FetchAndUpdateCityData.as_view(), name='city-info'),
    path('', include(router.urls)),

]
