from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserAccountSerializer
import re
import logging

logger = logging.getLogger(__name__)


# NOTE: API endpoint to subscribe to the newsletter
@api_view(["POST"])
def subscribe_newsletter(request):
    email = request.data.get("email", "")

    # Validate email format with ".com" ending
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[cC][oO][mM]$"
    if not re.match(email_regex, email):
        logger.warning("Invalid email format")
        return Response(
            {"email": 'Invalid email format. Must end with ".com".'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = UserAccountSerializer(data=request.data)
    if serializer.is_valid():
        logging.info("Email format is valid")
        serializer.save()
        return Response(
            {"message": "Successfully subscribed!"}, status=status.HTTP_201_CREATED
        )
    logging.error("Email format is invalid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
