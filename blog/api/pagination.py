from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
