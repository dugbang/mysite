import os
from datetime import datetime

from django.db import models

# Create your models here.
from django.urls import reverse


class Plant(models.Model):
    """
    작물별 cvs 파일을 갖을 경우 문제있는 작물에 대응하기 힘듬. >> 별도의 모델로 관리
    """
    name = models.CharField(max_length=100, unique=True)
    # note = models.CharField(max_length=255)
    # file = models.FileField
    # JSON 으로 DateTimeField 를 전송할 수 있는지 확인하기 위함
    create_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('ezp10:plant_detail', args=(self.id,))


def _get_upload_path_actuator(instance, filename):
    et = datetime.now()
    year = et.strftime('%Y')
    month = et.strftime('%m')
    # str_time = '{}'.format(datetime.now())[:19]
    # filename; 상추_20180712.cvs
    # TODO; #583 참조
    # 파일정보를 로그로 출력하여 보기.
    return os.path.join('actuator', '{}'.format(instance.serial), year, month, filename)


class Controller(models.Model):
    """
    pk에 의해 정보 처리가 적절하지 않을 경우 serial 을 PK 로 설정하는 것을 고려해보자.
    serial = models.CharField(max_length=16, primary_key=True)
    """
    # serial = models.CharField('serial', max_length=16, unique=True)
    serial = models.CharField(max_length=16, primary_key=True)

    is_active = models.BooleanField(default=False)

    # TODO; 다른 모델과 같이 추가되어야 함.
    # owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    plant = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)

    minute_of_action_cycle = models.IntegerField(default=1)
    minute_of_upload_cycle = models.IntegerField(default=5)

    iis_tank_capacity = models.BooleanField(default=False)
    iis_temperature = models.BooleanField(default=False)
    iis_ph = models.BooleanField(default=False)
    iis_mc = models.BooleanField(default=False)
    iis_temp_humidity_high = models.BooleanField(default=False)
    iis_temp_humidity_low = models.BooleanField(default=False)
    iis_luminance = models.BooleanField(default=False)
    iis_co2 = models.BooleanField(default=False)

    ois_led = models.BooleanField(default=False)
    ois_pump = models.BooleanField(default=False)
    ois_pan_high = models.BooleanField(default=False)
    ois_pan_low = models.BooleanField(default=False)

    is_usb_camera = models.BooleanField(default=False)

    # modify_date = models.CharField('Modify Date', max_length=19)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    # actuator_url = models.URLField('actuator url', blank=True)
    actuator_csv = models.FileField(upload_to=_get_upload_path_actuator)

    capture_times = models.CharField('capture times', max_length=255, default='0900,1200,1800')
    stable_time_of_camera = models.IntegerField(default=5)

    class Meta:
        ordering = ('serial', 'is_active', 'plant')

    def __str__(self):
        return self.serial

    # def get_absolute_url(self):
    #     return reverse('ezp10:capture_detail', args=(self.id,))


# class Actuator(models.Model):
#     controller = models.ForeignKey(Controller, on_delete=models.DO_NOTHING)
#
#     upload = models.FileField(upload_to=_get_upload_path_actuator)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('controller', )
#
#     def __str__(self):
#         return self.upload.name
#
#     # def get_absolute_url(self):
#     #     return reverse('ezp10:capture_detail', args=(self.id,))


def _get_upload_path_capture(instance, filename):
    # str_time = '{}'.format(datetime.now())[:19]
    return os.path.join('capture', '{}'.format(instance.controller.serial),
                        '{}'.format(instance.plant.name), filename)


class Capture(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)
    controller = models.ForeignKey(Controller, on_delete=models.DO_NOTHING)

    image = models.ImageField(upload_to=_get_upload_path_capture)

    # create_at = models.CharField('Create Date', max_length=19, null=True)
    create_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ('plant', 'controller', 'create_at', )

    def __str__(self):
        return self.image.name

    # def get_absolute_url(self):
    #     return reverse('ezp10:capture_detail', args=(self.id,))


class Report(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.DO_NOTHING)
    controller = models.ForeignKey(Controller, on_delete=models.DO_NOTHING)

    # create_at = models.CharField('Create Date', max_length=19, null=True)
    # create_at = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(null=True)

    tank_capacity = models.CharField(max_length=20, default='0')
    temperature = models.CharField(max_length=20, default='0')
    ph = models.CharField(max_length=20, default='0')
    mc = models.CharField(max_length=20, default='0')
    temp_humidity_high = models.CharField(max_length=20, default='0')
    temp_humidity_low = models.CharField(max_length=20, default='0')
    luminance = models.CharField(max_length=20, default='0')
    co2 = models.CharField(max_length=20, default='0')

    on_off_led = models.BooleanField(default=False)
    on_off_pump = models.BooleanField(default=False)
    on_off_pan_high = models.BooleanField(default=False)
    on_off_pan_low = models.BooleanField(default=False)

    class Meta:
        ordering = ('plant', 'controller', 'create_at')

    # def __str__(self):
    #     return self.image.name
    #
    # def get_absolute_url(self):
    #     return reverse('ezp10:capture_detail', args=(self.id,))

