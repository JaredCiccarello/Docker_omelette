from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Eggs


class EggsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_eggs = Eggs.objects.create(name="rake", owner=testuser1, description="Better for collecting leaves than shovel.")
        test_eggs.save()

    def test_egg_model(self):
        eggs = Eggs.objects.get(id=1)
        actual_owner = str(eggs.owner)
        actual_name = str(eggs.name)
        actual_description = str(eggs.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(actual_description, "Better for collecting leaves than shovel.")

# Create your tests here.
