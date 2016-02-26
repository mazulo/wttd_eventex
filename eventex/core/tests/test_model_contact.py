from django.test import TestCase
from django.core.exceptions import ValidationError

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Patrick Mazulo',
            slug='patrick-mazulo',
            photo='http://bit.ly/mazulo-pic'
        )

    def test_email(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='pmazulo@gmail.com'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='86-999887848'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='A',
            value='B'
        )
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='pmazulo@gmail.com'
        )
        self.assertEqual('pmazulo@gmail.com', str(contact))
