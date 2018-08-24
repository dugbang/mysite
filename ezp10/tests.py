import logging

from django.test import TestCase

# Create your tests here.
from ezp10.models import Plant

ezp10_logger = logging.getLogger(__name__)


class PlantModelTests(TestCase):

    def test_plant_동작확인(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        plant = Plant(name='배추')
        # ezp10_logger.debug(plant.__dict__['id'])
        # ezp10_logger.debug(plant.dic())
        print(plant.dic())
        self.assertIs(plant.__dict__['name'] == '상추', False)
        self.assertIs(plant.__dict__['name'] == '배추', True)

        Plant.objects.create(name='무우')
        Plant.objects.create(name='상추')
        Plant.objects.create(name='배추')
        print(Plant.objects.count())
