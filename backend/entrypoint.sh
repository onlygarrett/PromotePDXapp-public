#!/bin/sh

# Debugging: Print environment variables
echo "Environment Variables:"
env

until cd /app/backend/; do
  echo "Waiting for server volume..."
done

until ./manage.py migrate --noinput; do
  echo "Waiting for db to be ready..."
  sleep 2
done

echo "Collecting static files..."
python3 manage.py collectstatic --noinput
echo "Static files collected"

echo "Creating default superuser..."
python3 manage.py auto_createsuperuser
echo "superuser created"

echo "Running initial sheets refresh..."
python3 manage.py refresh_events
echo "Initial sheets refreshed"

# Create weekly periodic task if it doesn't exist
python manage.py shell <<EOF
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
from json import dumps

try:
    # # Task Name
    # task_name = "Send Weekly Newsletter"
    #
    # # Create schedule (weekly)
    # schedule, created = IntervalSchedule.objects.get_or_create(
    #     every=7,
    #     period=IntervalSchedule.DAYS,
    # )
    #
    # # Check if task already exists
    # task, created = PeriodicTask.objects.get_or_create(
    #     name=task_name,
    #     defaults={
    #         "interval": schedule,
    #         "task": "UserAccounts.tasks.send_newsletter",  # Replace with your task path
    #         "args": dumps([]),  # Optional: Empty arguments
    #         "enabled": True  # Ensure it's enabled
    #     }
    # )
    #
    # # If task exists but is disabled, enable it
    # if not created and not task.enabled:
    #     task.enabled = True
    #     task.save()
    #     print("Enabled existing periodic task: Weekly Newsletter")
    # elif created:
    #     print("Created periodic task: Weekly Newsletter")
    # else:
    #     print("Periodic task already exists and is enabled.")


    # Task Name for daily task
    daily_task_name = "Daily Sheets Refresh"

    # Create schedule (daily at midnight)
    daily_schedule, created = CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="0",
    )

    # Check if daily task already exists
    daily_task, created = PeriodicTask.objects.get_or_create(
        name=daily_task_name,
        defaults={
            "crontab": daily_schedule,
            "task": "EventCalendar.tasks.daily_sheets_refresh",  # Updated task path
            "args": dumps([]),  # Optional: Empty arguments
            "enabled": True  # Ensure it's enabled
        }
    )

    # If daily task exists but is disabled, enable it
    if not created and not daily_task.enabled:
        daily_task.enabled = True
        daily_task.save()
        print("Enabled existing periodic task: Daily Sheets Refresh")
    elif created:
        print("Created periodic task: Daily Sheets Refresh")
    else:
        print("Periodic task already exists and is enabled.")

except Exception as e:
    print(f"Error configuring periodic task: {e}")
EOF

echo "Starting Gunicorn..."
exec gunicorn promotepdxapp.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4
