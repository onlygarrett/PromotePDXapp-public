from django.core.cache import cache
from django.test import TestCase
from EventCalendar.models import Event


class EventCacheTestCase(TestCase):
    def setUp(self):
        """
        Create test event and set cache.
        """
        self.event = Event.objects.create(
            artist="Cached Artist", date="2025-07-10", venue="Venue C")
        cache.set("test_event_cache", {
                  "artist": self.event.artist, "date": self.event.date}, timeout=60)

    def test_event_cache(self):
        """
        Test if event data is stored in Redis cache.
        """
        cached_event = cache.get("test_event_cache")
        self.assertIsNotNone(cached_event)
        self.assertEqual(cached_event["artist"], "Cached Artist")

    def test_cache_expiry(self):
        """
        Test if cached data expires properly.
        """
        cache.set("test_event_temp", {
                  "test": "data"}, timeout=1)  # 1 second expiry
        import time
        time.sleep(2)
        self.assertIsNone(cache.get("test_event_temp"))
