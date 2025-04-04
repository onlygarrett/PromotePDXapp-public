from django.test import TestCase
from django.urls import reverse
from EventCalendar.models import Event


class EventPaginationTestCase(TestCase):
    def setUp(self):
        """
        Create multiple test events.
        """
        for i in range(50):  # Creating 50 events for pagination
            Event.objects.create(
                artist=f"Artist {i}", date="2025-06-10", venue="Venue X")

    def test_event_pagination(self):
        """
        Test pagination functionality.
        """
        response = self.client.get(
            reverse('events-list'), {'page': 1})  # First page
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.json())  # Ensure paginated response
        self.assertLessEqual(
            len(response.json()["results"]), 32)  # Per-page limit

    def test_event_filter_pagination(self):
        """
        Test pagination along with filtering.
        """
        response = self.client.get(
            reverse('events-list'), {'artist': 'Artist 1', 'page': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            any(event['artist'] == 'Artist 1' for event in response.json()["results"]))
