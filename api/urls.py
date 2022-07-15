from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'terms', views.TermViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'styles', views.SttyleViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls
