from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from decouple import config
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPERUSER_USERNAME', cast=str)
DJANGO_SUPERUSER_PASSWORD = config('DJANGO_SUPERUSER_PASSWORD', cast=str)
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL', cast=str)


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        try:
            User = get_user_model()

            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username=DJANGO_SUPERUSER_USERNAME, email=DJANGO_SUPERUSER_EMAIL, password=DJANGO_SUPERUSER_PASSWORD)
                self.stdout.write(self.style.SUCCESS(
                    'Successfully created new superuser'))
            else:
                logger.info('Superuser already exists in the database')

        except Exception as e:
            raise CommandError(e)
