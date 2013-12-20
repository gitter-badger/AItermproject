import datetime

from django.utils import timezone
from django.test import TestCase

from events.models import Event

class EventMethodTests(TestCase):

    def test_was_published_recently_with_future_event(self):
        """
        was_published_recently() should return False for events whose
        pub_date is in the future
        """
        future_event = Event(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_event.was_published_recently(), False)
    def test_was_published_recently_with_old_event(self):
        """
        was_published_recently() should return False for events whose pub_date
        is older than 1 day
        """
        old_event = Event(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_event.was_published_recently(), False)

    def test_was_published_recently_with_recent_event(self):
        """
        was_published_recently() should return True for events whose pub_date
        is within the last day
        """
        recent_event = Event(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_event.was_published_recently(), True)