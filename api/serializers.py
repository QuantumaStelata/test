from rest_framework import serializers

from main.models import Term, Brand, Style


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"


class SearchSerializer(serializers.Serializer):
    term_id = serializers.IntegerField(allow_null=True)
    brand_id = serializers.IntegerField(allow_null=True)
    style_id = serializers.IntegerField(allow_null=True)
