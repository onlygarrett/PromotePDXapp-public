import logging
from datetime import datetime

from django.db.models import Count
from django.utils.dateparse import parse_date

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

logger = logging.getLogger(__name__)


@api_view(["GET"])
def events(request):
    logger.info("GET events endpoint hit")
    paginator = PageNumberPagination()
    paginator.page_size = 32  # Set number of items per page

    # Retrieve the 'artist' query parameter
    artist_query = request.GET.get("artist", None)
    start_date = request.GET.get("start_date", None)
    end_date = request.GET.get("end_date", None)
    venue = request.GET.get("venue", None)
    # Default sort by 'start_date'
    sort_by = request.GET.get("sort_by", "date")
    order = request.GET.get("order", "asc")  # Default ascending order

    # Query events and paginate them
    events = Event.objects.all()  # Order by latest
    if artist_query:
        events = events.filter(artist__icontains=artist_query)
    if venue:
        events = events.filter(venue__icontains=venue)

    if start_date:
        # Date greater than or equal to start_date
        events = events.filter(date__gte=parse_date(start_date))
    if end_date:
        # Date less than or equal to end_date
        events = events.filter(date__lte=parse_date(end_date))
    events = events.order_by(sort_by)  # order

    result_page = paginator.paginate_queryset(events, request)

    # Serialize data
    serializer_data = EventSerializer(result_page, many=True).data

    # Format the date field
    for event in serializer_data:
        event["date"] = datetime.strptime(event["date"], "%Y-%m-%d").strftime(
            "%B %d, %Y"
        )

    # Return paginated response
    logger.info("Returning paginated response")
    return paginator.get_paginated_response(serializer_data)


@api_view(["GET"])
def venues(request):
    logger.info("GET venues endpoint hit")
    venues = (
        Event.objects.values("venue").annotate(
            count=Count("venue")).order_by("venue")
    )
    venue_list = [venue["venue"] for venue in venues]
    return Response(venue_list)
