from celery import shared_task
from django.core.mail import send_mail
from .models import UserAccount
import logging

logger = logging.getLogger(__name__)


# NOTE: This is a Task to create a news letter to be used with a celery worker.
@shared_task
def send_newsletter():
    subject = "Newsletter Update"
    message = """
    Hello,

    ...

    Stay tuned for more updates!

    Regards,
    Your Team
    """
    sender = "XXXtestemailXXX@gmail.com"  # TODO: Replace with your email

    recipients = UserAccount.objects.values_list("email", flat=True)

    if recipients:
        logger.info("Recipients pulled. Sending newsletter to recipients")
        send_mail(subject, message, sender, recipients, fail_silently=False)
