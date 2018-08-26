from rest_framework import serializers

from ezp10.models import Plant


class PlantSerializerFunc(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('name', )
