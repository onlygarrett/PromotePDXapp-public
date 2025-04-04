from django.core.management.base import BaseCommand, CommandError
from decouple import config
import logging
from EventCalendar.admin import EventAdmin

logger = logging.getLogger(__name__)

DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPERUSER_USERNAME', cast=str)
DJANGO_SUPERUSER_PASSWORD = config('DJANGO_SUPERUSER_PASSWORD', cast=str)
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL', cast=str)


class Command(BaseCommand):
    help = 'Refresh and pull in events from sheets.'

    def handle(self, *args, **options):
        try:
            EventAdmin.run_sheets_refresh()
            logger.info("Sheets refresh completed successfully.")
        except Exception as e:
            logger.error(f"Error during sheets refresh: {e}")
            raise CommandError(e)
