from django.test import TestCase

from eventex.subscriptions.models import Subscription

from datetime import datetime


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
                name='Patrick Mazulo',
                cpf='03286218383',
                email='pmazulo@gmail.com',
                phone='86-99988-7848'

        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)
