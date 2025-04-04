from celery import shared_task
from .admin import EventAdmin
import logging

logger = logging.getLogger(__name__)


@shared_task
def daily_sheets_refresh():
    try:
        EventAdmin.run_sheets_refresh()
        logger.info("Daily sheets refresh task completed successfully.")
    except Exception as e:
        logger.error(f"Error during daily sheets refresh task: {e}")
