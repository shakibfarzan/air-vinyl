from rest_framework.pagination import PageNumberPagination

LIST_CREATE_MODEL_VIEW_SET = {"get": "list", "post": "create"}
DETAIL_MODEL_VIEW_SET = {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 200