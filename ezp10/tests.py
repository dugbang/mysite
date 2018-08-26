import json
import logging

from django.test import TestCase, RequestFactory, Client

# Create your tests here.
from django.urls import reverse
from rest_framework import status

from ezp10.models import Plant
from ezp10.serializers import PlantSerializerFunc
from ezp10.views import PlantLV

ezp10_logger = logging.getLogger(__name__)

# initialize the APIClient app
client = Client()


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


class TestModelPlant(TestCase):

    def setUp(self):
        self.plants = [
            Plant.objects.create(name='사과'),
            Plant.objects.create(name='바나나'),
            Plant.objects.create(name='고추'),
        ]
        self.rec_count = 3

    def test_plant_count(self):
        self.assertEqual(Plant.objects.count(), self.rec_count)

    def test_get_all_plants(self):
        # get API response
        # response = client.get(reverse('get_post_plants'))
        response = client.get('/ezp10/api-f/plant/')
        # get data from db
        plants = Plant.objects.all()
        serializer = PlantSerializerFunc(plants, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_plant(self):
        # response = client.get(reverse('get_delete_update_puppy', kwargs={'pk': 30}))
        response = client.get('/ezp10/api-f/plant/300')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid_single_plant(self):
        # response = client.get(reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}))
        response = client.get('/ezp10/api-f/plant/{}'.format(self.plants[0].pk))
        plant = Plant.objects.get(pk=self.plants[0].pk)
        serializer = PlantSerializerFunc(plant)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_plant(self):
        self.valid_payload = {
            'name': '상추',
        }
        response = client.post(
            # reverse('plant_api_post'),
            '/ezp10/api-f/plant/',
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
            # reverse('plant_api_post'),
            '/ezp10/api-f/plant/',
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
    #         '/ezp10/api-f/plant/',
    #         data=json.dumps(multi_data),
    #         content_type='application/json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class PlantModelTests(TestCase):
#
#     def test_plant_동작확인(self):
#         """
#         was_published_recently() returns False for questions whose pub_date
#         is in the future.
#         """
#         plant = Plant(name='배추')
#         # ezp10_logger.debug(plant.__dict__['id'])
#         # ezp10_logger.debug(plant.dic())
#         print(plant.dic())
#         self.assertIs(plant.__dict__['name'] == '상추', False)
#         self.assertIs(plant.__dict__['name'] == '배추', True)
#
#         Plant.objects.create(name='무우')
#         Plant.objects.create(name='상추')
#         Plant.objects.create(name='배추')
#         print(Plant.objects.count())
