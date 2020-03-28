from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Toy

from toyApp.serializers import ToySerializer


TOYS_URL = reverse('toys:toy-list')


def sample_toy():
    """Create and return a sample toy"""
    defaults = {
        'name': 'Sample toy',
        'description': 'Sample desc',
        'toy_category': 'xyz',
        'was_included_in_home': 'True'
    }
    return Toy.objects.create(**defaults)
    

class ToyApiTest(TestCase):
    """Test the toy API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieving_toy(self):
        """Test retriewing a list of toys"""
        sample_toy()
        sample_toy()

        res = self.client.get(TOYS_URL)

        toys = Toy.objects.all()
        serializer = ToySerializer(toys, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
