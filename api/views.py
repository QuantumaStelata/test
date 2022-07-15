from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import TermSerializer, BrandSerializer, StyleSerializer, SearchSerializer
from main.models import Term, Brand, Style


class TermViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Term.objects.all().order_by('id')
    serializer_class = TermSerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer


class StyleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Style.objects.all().order_by('id')
    serializer_class = StyleSerializer


class SearchApiView(GenericAPIView):
    serializer_class = SearchSerializer

    def get(self, request, *args, **kwargs):
        term_slug = request.GET.get('s')
        brand_slug = request.GET.get('b')
        style_slug = request.GET.get('st')

        term = brand = style = None

        if term_slug:
            term = Term.objects.filter(slug=term_slug).first()
        
        if brand_slug:
            brand = Brand.objects.filter(slug=brand_slug).first()
        
        if style_slug:
            style = Style.objects.filter(slug=style_slug).first()

        data = {
            "term_id": term.id if term else None,
            "brand_id": brand.id if brand else None,
            "style_id": style.id if style else None,
        }

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"status": "error"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
