import logging
from email.utils import formatdate

import pandas as pd
from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django_object_actions import (
    DjangoObjectActions,
)
from EventCalendar.models import Event

logger = logging.getLogger(__name__)


class CsvHandlerForm(forms.Form):
    csv_file = forms.FileField()


class EventAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = (
        "artist",
        "date",
        "venue",
        "time",
        "link",
        "sold_out",
        "ages",
        "price",
        "exclude",
    )

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("upload-csv/", self.upload_csv),
            path("sheets-refresh/", self.sheets_refresh),
        ]
        return new_urls + urls

    def upload_csv(modeladmin, request, queryset):
        logger.info("Starting upload")

        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            if not csv_file.name.endswith(".csv"):
                logger.warning("Incorrect file selected")
                messages.warning(
                    request, "The wrong type of file was uploaded")
                return HttpResponseRedirect(request.path_info)

            file_data = pd.read_csv(
                csv_file,
                header=0,
                names=[
                    "Date",
                    "Venue",
                    "Time",
                    "Artist",
                    "Website",
                    "Sold out?",
                    "Ages",
                    "Ticket Price",
                    "ExcludeFromWeekly",
                ],
                encoding="utf8",
                converters={
                    "Sold out?": lambda x: False if x == "False" else True,
                    "Ticket Price": lambda x: x.replace("$", "")
                    .replace(",", "")
                    .replace("free", "")
                    .replace("Free", ""),
                    "ExcludeFromWeekly": lambda x: False if x == "False" else True,
                },
                parse_dates=True,
            )

            # Check if date format is correct
            count = Event.refresh_calendar_data(file_data)

            file_data.to_csv("./static/backup/calendar.csv")
            url = reverse("admin:index")
            logger.info("Upload successful")
            return HttpResponseRedirect(url)

        form = CsvHandlerForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

    def sheets_refresh(modeladmin, request, queryset):
        print("Refresh button pushed")
        logger.info("Starting refresh")
        events = Event.return_sheets_rows()
        count = Event.refresh_calendar_data(events)

        url = reverse("admin:index")
        return HttpResponseRedirect(url)

    @classmethod
    def run_sheets_refresh(cls):
        logger.info("Running sheets refresh")
        request = HttpRequest()
        queryset = Event.objects.all()
        admin_instance = cls(Event, admin.site)
        admin_instance.sheets_refresh(request, queryset)
        logger.info("Sheets refresh completed")

    changelist_actions = (
        "sheets_refresh",
        "upload_csv",
    )


admin.site.register(Event, EventAdmin)
