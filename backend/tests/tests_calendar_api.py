from django.test import TestCase
import pandas as pd
from EventCalendar.models import Event
from EventCalendar.serializers import EventSerializer


class EventTestCase(TestCase):
    def test_sheet_connection(self):
        """Test connection to the sheets database"""
        self.assertIsNotNone(Event.return_sheets_rows())

    def test_sheet_refresh_db(self):
        """Test connection to the sheets database and writing to db"""
        events = Event.return_sheets_rows()
        self.assertIsNotNone(events)
        count = Event.refresh_calendar_data(events)

        print("The Count was: " + str(count))

        self.assertGreater(count, 0)
        events = Event.objects.all()

        serializer = EventSerializer(events, many=True)
        self.assertIsNotNone(serializer.data)
        self.assertGreater(len(serializer.data), 0)

    def test_refresh_calendar_data_with_missing_dates(self):
        """Test refresh_calendar_data method with missing 'Date' field"""
        data = {
            "Artist": ["Artist 1", "Artist 2"],
            "Date": [None, "02/26/2025"],
            "Venue": ["Venue 1", "Venue 2"],
            "Time": ["8:00 PM", "9:00 PM"],
            "Website": ["http://example.com/1", "http://example.com/2"],
            "Sold out?": [False, True],
            "Ages": ["All Ages", "21+"],
            "Ticket Price": ["$10", "$20"],
            "ExcludeFromWeekly": [False, True]
        }
        event_data = pd.DataFrame(data)
        count = Event.refresh_calendar_data(event_data)

        print("The Count was: " + str(count))

        # Check that only one event was created
        self.assertEqual(count, 1)
        events = Event.objects.all()
        self.assertEqual(events.count(), 1)

        # Verify the created event
        event = events.first()
        self.assertEqual(event.artist, "Artist 2")
        self.assertEqual(event.date.strftime("%Y-%m-%d"), "2025-02-26")
        self.assertEqual(event.venue, "Venue 2")
        self.assertEqual(event.time, "9:00 PM")
        self.assertEqual(event.link, "http://example.com/2")
        self.assertTrue(event.sold_out)
        self.assertEqual(event.ages, "21+")
        self.assertEqual(event.price, "20")
        self.assertTrue(event.exclude)
