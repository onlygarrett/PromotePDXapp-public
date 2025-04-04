import datetime
import logging

import gspread
import pandas as pd
from django.db import models
from google.oauth2.service_account import Credentials
from pandas.io.parsers import TextFileReader
from promotepdxapp.settings import SCOPES

logger = logging.getLogger(__name__)


class Event(models.Model):
    artist = models.CharField("Artist", max_length=500)
    date = models.DateField("Date", blank=True, null=True)
    venue = models.CharField("Venue", max_length=120, blank=True, null=True)
    time = models.CharField("Time", max_length=120, blank=True, null=True)
    link = models.URLField("EventInfo", max_length=500, blank=True, null=True)
    sold_out = models.BooleanField("Sold Out", blank=True, null=True)
    ages = models.CharField("Ages", max_length=120, blank=True, null=True)
    price = models.CharField("Ticket Price", max_length=120, blank=True, null=True)
    exclude = models.BooleanField("Exclude From Weekly", blank=True, null=True)

    @staticmethod
    def return_sheets_rows():
        logger.info("Pulling sheets data...")
        creds = Credentials.from_service_account_file(
            "static/credentials.json", scopes=SCOPES
        )
        client = gspread.authorize(creds)

        sheet_id = "1nC2sJTHWggzEdpbxT-DCOiRLla4c_fjbi-BdMl0U4tM"
        sheet = client.open_by_key(sheet_id)
        sheet = sheet.worksheet("2022 Music Calendar")
        logger.info("Parsing data...")

        # Get raw data from sheet
        raw_data = sheet.get_all_values()
        if not raw_data:
            logger.error("Sheet is empty")
            return pd.DataFrame()

        # Create DataFrame and set headers from first row
        values_list = pd.DataFrame(raw_data)
        headers = values_list.iloc[0].tolist()

        # Validate required headers are present
        required_headers = [
            "Artist",
            "Date",
            "Venue",
            "Time",
            "Website",
            "Sold out?",
            "Ages",
            "Ticket Price",
            "ExcludeFromWeekly",
        ]

        # Create DataFrame and set headers from first row
        values_list = pd.DataFrame(raw_data)
        headers = values_list.iloc[0].tolist()

        # Validate required headers are present
        required_headers = [
            "Artist",
            "Date",
            "Venue",
            "Time",
            "Website",
            "Sold out?",
            "Ages",
            "Ticket Price",
            "ExcludeFromWeekly",
        ]
        missing_headers = [h for h in required_headers if h not in headers]

        if missing_headers:
            logger.error(f"Missing required headers: {', '.join(missing_headers)}")
            return pd.DataFrame()

        # Set headers and remove header row
        values_list.columns = headers
        values_list = values_list.iloc[1:]  # Remove header row
        logger.info("Data validated and pulled from sheets...")

        # Set headers and remove header row
        values_list.columns = headers
        values_list = values_list.iloc[1:]  # Remove header row
        logger.info("Data validated and pulled from sheets...")

        return values_list

    @staticmethod
    def refresh_calendar_data(
        event_data: pd.DataFrame | pd.Series | TextFileReader,
    ) -> int:
        logger.info("Refreshing calendar data...")
        count = 0

        # Clear existing data
        Event.objects.all().delete()
        logger.info("Existing calendar data cleared.")

        if isinstance(event_data, pd.DataFrame):
            csv_data = event_data.iterrows()
            for idx, x in csv_data:
                # Log the current row being processed
                logger.info(f"Processing row at index {idx}: {x.to_dict()}")

                # Check for valid artist name first
                artist = x.get("Artist", "").strip()
                if not artist:
                    logger.warning(f"Skipping row {idx}: Missing artist name")
                    continue

                # Handle date with proper null checking
                date_str = x.get("Date")
                event_date = None
                if date_str and not pd.isna(date_str):
                    try:
                        event_date = datetime.datetime.strptime(
                            date_str, "%m/%d/%Y"
                        ).strftime("%Y-%m-%d")
                    except ValueError:
                        logger.warning(f"Invalid date format for event: {artist}")

                # Handle ticket price with proper null checking
                raw_price = x.get("Ticket Price")
                ticket_price = ""
                if not pd.isna(raw_price):
                    price_str = str(raw_price).strip().lower()
                    if price_str == "free":
                        ticket_price = "0.0"
                    elif price_str:
                        ticket_price = price_str.replace("$", "").replace(",", "")

                # Safely extract remaining fields
                venue = x.get("Venue", "")
                time = x.get("Time", "")
                website = x.get("Website", "")
                ages = x.get("Ages", "")
                sold_out = bool(x.get("Sold out?", False))
                exclude = bool(x.get("ExcludeFromWeekly", False))

                Event.objects.create(
                    date=event_date,
                    venue=venue,
                    time=time,
                    artist=artist,
                    link=website,
                    sold_out=sold_out,
                    ages=ages,
                    price=ticket_price,
                    exclude=exclude,
                )
                count += 1
        logger.info("Data refreshed...")
        return count

    def __str__(self):
        return self.artist
