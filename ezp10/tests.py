import json
import logging
from datetime import datetime

from django.test import TestCase, RequestFactory, Client

# Create your tests here.
from django.urls import reverse
# from django.utils.datetime_safe import datetime
from rest_framework import status

from ezp10.models import Plant, Capture
from ezp10.serializers import CaptureSerializer, PlantSerializer
from ezp10.views import PlantLV

ezp10_logger = logging.getLogger(__name__)

# initialize the APIClient app
client = Client()


# class TestModelCapture(TestCase):
#
#     def setUp(self):
#         self.plants = [
#             Plant.objects.create(name='사과'),
#             Plant.objects.create(name='바나나'),
#             Plant.objects.create(name='고추'),
#         ]
#         self.plants_count = len(self.plants)
#
#         str_date = '{}'.format(datetime.now())[:19]
#         # str_date = datetime.now()
#         self.captures = [
#             Capture.objects.create(plant_id=self.plants[0], name='TDD test 0', create_date=str_date),
#             Capture.objects.create(plant_id=self.plants[0], name='TDD test 1', create_date=str_date),
#             Capture.objects.create(plant_id=self.plants[2], name='TDD test 2', create_date=str_date),
#             Capture.objects.create(plant_id=self.plants[1], name='TDD test 3', create_date=str_date),
#             Capture.objects.create(plant_id=self.plants[2], name='TDD test 4', create_date=str_date),
#         ]
#         self.captures_count = len(self.captures)
#
#     def test_captures_count(self):
#         self.assertEqual(Plant.objects.count(), self.plants_count)
#         self.assertEqual(Capture.objects.count(), self.captures_count)
#
#     def test_get_all_plants(self):
#         response = client.get(reverse('ezp10:capture_list'))
#         capture = Capture.objects.all()
#         serializer = CaptureSerializer(capture, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_invalid_single_plant(self):
#         response = client.get(reverse('ezp10:capture_detail', kwargs={'pk': 300}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_get_valid_single_plant(self):
#         response = client.get(reverse('ezp10:capture_detail', kwargs={'pk': self.captures[3].pk}))
#         capture = Capture.objects.get(pk=self.captures[3].pk)
#         serializer = CaptureSerializer(capture)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_create_valid_plant(self):
#         str_date = '{}'.format(datetime.now())[:19]
#
#         plant = Plant.objects.filter(name='고추')
#         ezp10_logger.debug(plant[0].id)
#
#         payload = {
#             'plant_id': plant[0].id,
#             'name': 'post insert...',
#             'create_date': str_date
#         }
#         response = client.post(
#             reverse('ezp10:capture_list'),
#             data=json.dumps(payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Capture.objects.count(), self.captures_count + 1)
#
#     def test_create_invalid_plant(self):
#         self.invalid_payload = {
#             'name': '',
#         }
#         response = client.post(
#             reverse('ezp10:capture_list'),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestModelPlant(TestCase):
    """
    TODO; 갱신/삭제 부분에 대한 테스트가 추가되어야 함.
    """
    def setUp(self):
        self.plants = [
            Plant.objects.create(name='사과'),
            Plant.objects.create(name='바나나'),
            Plant.objects.create(name='고추'),
        ]
        self.rec_count = 3
        # self.base_url = '/ezp10/api-f/plant/'
        self.base_url = '/ezp10/api/plant/'

    def test_plant_count(self):
        self.assertEqual(Plant.objects.count(), self.rec_count)

    def test_get_all_plants(self):
        # get API response
        response = client.get(reverse('ezp10:api_plant_list'))
        # response = client.get(self.base_url)
        # get data from db
        print('\nresponse.data; ', response.data)

        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_plant(self):
        response = client.get(reverse('ezp10:api_plant_detail', kwargs={'pk': 300}))
        # response = client.get('{}300'.format(self.base_url))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid_single_plant(self):
        response = client.get(reverse('ezp10:api_plant_detail', kwargs={'pk': self.plants[0].pk}))
        # response = client.get(reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}))
        # response = client.get('{}{}'.format(self.base_url, self.plants[0].pk))
        print('\nresponse.data; ', response.data)
        print(response.data['name'])
        # print(response.data['create_at'])

        plant = Plant.objects.get(pk=self.plants[0].pk)
        serializer = PlantSerializer(plant)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_plant(self):
        self.valid_payload = {
            'name': '상추',
        }
        response = client.post(
            reverse('ezp10:api_plant_list'),
            # self.base_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Plant.objects.count(), self.rec_count + 1)

    def test_create_invalid_plant(self):
        self.invalid_payload = {
            'name': '',
        }
        response = client.post(
            reverse('ezp10:api_plant_list'),
            # self.base_url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_create_array_valid_plant(self):
    #     # TODO; array data 전송 및 저장방법 개선.
    #     multi_data = {
    #         'data': [
    #             {'name': '배추'},
    #             {'name': '무우'}
    #         ]
    #     }
    #     response = client.post(
    #         # reverse('get_post_puppies'),
    #         self.base_url,
    #         data=json.dumps(multi_data),
    #         content_type='application/json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        # self.user = User.objects.create_user(
        #     username='jacob', email='jacob@…', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/ezp10/plant/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        # request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        # response = PlantLV(request)
        # Use this syntax for class-based views.
        response = PlantLV.as_view()(request)
        self.assertEqual(response.status_code, 200)

