from django.test import TestCase
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from json import dumps


class PeriodicTaskTest(TestCase):

    def setUp(self):
        """
        Create periodic tasks required for testing.
        """
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=7,
            period=IntervalSchedule.DAYS,
        )
        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name="Send Weekly Newsletter",
            task="UserAccounts.tasks.send_newsletter",
            defaults={'args': dumps([]), 'enabled': True}
        )

    def test_periodic_task_created(self):
        """
        Test that the periodic task exists and is enabled.
        """
        task = PeriodicTask.objects.get(name="Send Weekly Newsletter")
        self.assertTrue(task.enabled)
