from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.core import exceptions

from conference.models import Conference


class ConferenceTest(TestCase):
    def test_multiple_enable(self):
        """
        Test that there can only be one conference enabled at a time.
        """
        pycon = Conference(name='PyCon Philippines 2012',
                           starts=timezone.now(),
                           ends=timezone.now() + timedelta(days=1),
                           description='Python Conference Philippines 2012',
                           is_enabled=True)
        pycon.save()

        pycon = Conference(name='PyCon Philippines 2013',
                           starts=timezone.now(),
                           ends=timezone.now() + timedelta(days=1),
                           description='Python Conference Philippines 2013',
                           is_enabled=True)
        self.assertRaises(exceptions.ValidationError, pycon.full_clean)
