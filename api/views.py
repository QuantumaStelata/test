from rest_framework import viewsets
from rest_framework import permissions

from .serializers import TermSerializer, BrandSerializer, StyleSerializer
from main.models import Term, Brand, Style


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all().order_by('id')
    serializer_class = TermSerializer
    http_method_names = ('get',)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer
    http_method_names = ('get',)


class SttyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all().order_by('id')
    serializer_class = StyleSerializer
    http_method_names = ('get',)
