from rest_framework import reverse
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class EventLimitOffsetPagination(PageNumberPagination):
    default_limit = 10
    max_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link() if self.page.has_previous() else None,
            },
            'count': self.count,
            'results': data
        })

    def get_next_link(self):
        if self.page.has_next():
            return reverse('book-list', kwargs={'page': self.page.next_page_number()})
        return None

    def get_previous_link(self):
        if self.page.has_previous():
            return reverse('book-list', kwargs={'page': self.page.previous_page_number()})
        return None
