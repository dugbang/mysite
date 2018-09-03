import logging

from rest_framework import serializers

from ezp10.models import Plant, Capture, Report, Controller

ezp10_logger = logging.getLogger(__name__)


class PlantSerializer(serializers.ModelSerializer):
    # ModelSerializer 를 이용해서 아래와 같이 짧은 코드로 직렬화 필드를 정의할 수 있다
    class Meta:
        model = Plant
        fields = ('name', 'create_at')

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Plant.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance


class CaptureSerializer(serializers.ModelSerializer):
    """
    plant = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)
    controller = models.ForeignKey(Controller, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=_get_upload_path_capture)
    create_date = models.CharField('Create Date', max_length=19, null=True)
    """
    # ModelSerializer 를 이용해서 아래와 같이 짧은 코드로 직렬화 필드를 정의할 수 있다
    class Meta:
        model = Capture
        # TODO; 모델 갱신시 반영.
        fields = ('plant', 'controller', 'create_date', )

    # 신규 instance 를 생성해서 리턴해준다
    def create(self, validated_data):
        return Capture.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    # def update(self, instance, validated_data):
    #     instance.plant = validated_data.get('plant', instance.plant)
    #     instance.controller = validated_data.get('controller', instance.controller)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.create_date = validated_data.get('name', instance.create_date)
    #     instance.save()
    #     return instance


class ReportSerializer(serializers.ModelSerializer):
    # TODO; 정보 일치시키기.
    class Meta:
        model = Report
        fields = ('plant', 'controller', 'create_at',
                  'tank_capacity', 'temperature', 'ph', 'mc',
                  'temp_humidity_high', 'temp_humidity_low', 'luminance', 'co2',
                  'on_off_led', 'on_off_pump', 'on_off_pan_high', 'on_off_pan_low',
                  )

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Report.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance


class ControllerSerializer(serializers.ModelSerializer):
    # TODO; 정보 일치시키기.
    class Meta:
        model = Controller
        fields = ('serial', 'is_action', 'plant',
                  'minute_of_action_cycle', 'minute_of_upload_cycle',
                  'iis_tank_capacity', 'iis_temperature', 'iis_ph', 'iis_mc',
                  'iis_temp_humidity_high', 'iis_temp_humidity_low', 'iis_luminance', 'iis_co2',
                  'ois_led', 'ois_pump', 'ois_pan_high', 'ois_pan_low',
                  'is_usb_camera', 'modify_date', 'actuator_csv',
                  'capture_times', 'stable_time_of_camera')

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Controller.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

