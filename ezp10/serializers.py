import logging

from rest_framework import serializers

from ezp10.models import Plant, Capture

ezp10_logger = logging.getLogger(__name__)


class PlantSerializerFunc(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('name', )


class PlantSerializer(serializers.ModelSerializer):
    # ModelSerializer 를 이용해서 아래와 같이 짧은 코드로 직렬화 필드를 정의할 수 있다
    class Meta:
        model = Plant
        fields = ('name', )

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Plant.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CaptureSerializer(serializers.ModelSerializer):
    # ModelSerializer 를 이용해서 아래와 같이 짧은 코드로 직렬화 필드를 정의할 수 있다
    class Meta:
        model = Capture
        # TODO; 모델 갱신시 반영.
        fields = ('plant_id', 'name', 'create_date', )

    # 신규 instance 를 생성해서 리턴해준다
    def create(self, validated_data):
        return Capture.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.plant_id = validated_data.get('plant_id', instance.plant_id)
        instance.name = validated_data.get('name', instance.name)
        instance.create_date = validated_data.get('name', instance.create_date)
        instance.save()
        return instance

