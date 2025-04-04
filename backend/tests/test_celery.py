from django.test import TestCase
from unittest.mock import patch
from UserAccounts.tasks import send_newsletter


class CeleryTaskTestCase(TestCase):
    @patch("UserAccounts.tasks.send_newsletter.apply_async")
    def test_send_newsletter_task(self, mock_task):
        """
        Test that the Celery task is triggered properly.
        """
        send_newsletter.apply_async()
        mock_task.assert_called_once()
