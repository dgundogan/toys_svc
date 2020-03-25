from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def test_create_toy_creation(self):
        """Test the toy creation"""
        toy = models.Toy.objects.create(
            name="test",
            description="desc",
            toy_category="test",
            release_date='2020-03-19',
            was_included_in_home=False
        )
