from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
import os


class SuperuserCreationTest(TestCase):

    def setUp(self):
        """
        Set environment variables required for superuser creation.
        """
        os.environ['DJANGO_SUPERUSER_USERNAME'] = 'jeeadmin'
        os.environ['DJANGO_SUPERUSER_EMAIL'] = 'admin@admin.com'
        os.environ['DJANGO_SUPERUSER_PASSWORD'] = '4545'

    def test_auto_createsuperuser_command(self):
        """
        Test that the 'auto_createsuperuser' command creates a superuser.
        """
        # Call the management command
        call_command('auto_createsuperuser')

        # Retrieve the created user
        User = get_user_model()
        user = User.objects.filter(username='jeeadmin').first()

        # Assertions
        self.assertIsNotNone(user)  # Superuser should exist
        self.assertTrue(user.is_superuser)  # Should have superuser privileges
        self.assertTrue(user.is_staff)  # Should have staff privileges
