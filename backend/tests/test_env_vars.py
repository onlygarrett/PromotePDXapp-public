from django.test import TestCase
from django.conf import settings
import os


class EnvVariableTest(TestCase):
    def test_env_variables_loaded(self):
        """
        Test that critical environment variables are loaded properly.
        """
        # Assert required variables exist
        self.assertEqual(settings.CELERY_BROKER_URL, "redis://redis:6379/0")
        self.assertEqual(settings.CELERY_RESULT_BACKEND, "django-db")

        # Check email environment variables
        self.assertEqual(settings.EMAIL_HOST, os.getenv("EMAIL_HOST", "smtp.gmail.com"))

        self.assertEqual(int(settings.EMAIL_PORT), int(os.getenv("EMAIL_PORT", 587)))
        self.assertEqual(settings.EMAIL_HOST_USER, os.getenv("EMAIL_HOST_USER"))
        self.assertTrue(settings.EMAIL_USE_TLS)

        # Redis configuration
        self.assertEqual(
            settings.CELERY_BROKER_URL, os.getenv("REDIS_URL", "redis://redis:6379/0")
        )

        # Periodic tasks and Django-Celery settings
        self.assertIn("django_celery_beat", settings.INSTALLED_APPS)
        self.assertIn("django_celery_results", settings.INSTALLED_APPS)
