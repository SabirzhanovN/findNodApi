from rest_framework import serializers


class GcdInputSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()