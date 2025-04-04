from django.test import TestCase
from django.urls import reverse
from EventCalendar.models import Event


class EventAPITestCase(TestCase):
    def setUp(self):
        """
        Create test events.
        """
        self.event1 = Event.objects.create(
            artist="Artist A", date="2025-06-01", venue="Venue A")
        self.event2 = Event.objects.create(
            artist="Artist B", date="2025-06-05", venue="Venue B")

    def test_event_list_api(self):
        """
        Test if the API returns event data correctly.
        """
        response = self.client.get(
            reverse('events-list'))  # Adjust based on your URL name
        self.assertEqual(response.status_code, 200)
        # Ensure events are returned
        self.assertGreater(len(response.json()), 0)

    def test_event_filter_by_artist(self):
        """
        Test filtering events by artist name.
        """
        response = self.client.get(
            reverse('events-list'), {'artist': 'Artist A'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['artist'], 'Artist A')
