from django.urls import reverse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.test import APIClient, APITestCase

LIST_CREATE_MODEL_VIEW_SET = {"get": "list", "post": "create"}
DETAIL_MODEL_VIEW_SET = {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 200

def is_sorted(array, *args, **kwargs) -> bool:
    order = kwargs.get('order')
    is_asc = order == 'asc'
    is_desc = order == 'desc'
    for i in range(0, len(array) - 1):
        if (array[i] > array[i+1] and is_asc) or (array[i] < array[i+1] and is_desc):
            return False
    return True

def test_ordering(test_case: APITestCase, ordering_fields: list[str], url_name: str):
    base_url = reverse(url_name) + "?ordering="
    def test_res(arg: str):
        url = base_url + arg
        response = test_case.client.get(url)
        test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data["results"]
        sorted_array = [item[arg] for item in results]
        test_case.assertTrue(is_sorted(sorted_array, order="asc"))
        
        url = base_url + "-" + arg
        response = test_case.client.get(url)
        test_case.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data["results"]
        sorted_array = [item[arg] for item in results]
        test_case.assertTrue(is_sorted(sorted_array, order="desc"))
    for e in ordering_fields:
        test_res(e)