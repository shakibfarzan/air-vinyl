from datetime import datetime
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from airvinyl.utils.general import test_ordering
from users.models import NormalUser

from users.tests.factories import NormalUserFactory, PremiumPlanFactory, SuperAdminFactory

class NormalUserListTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.ordering_fields = NormalUser.ORDERING_FIELDS
        self.super_admin = SuperAdminFactory()

        self.premium_plan_1 = PremiumPlanFactory(type="type 1", duration=3)
        self.premium_plan_2 = PremiumPlanFactory(type="type 2", duration=6)

        self.normal_user1 = NormalUserFactory(premium_plan=self.premium_plan_1)
        self.normal_user2 = NormalUserFactory(premium_plan=self.premium_plan_1)
        self.normal_user3 = NormalUserFactory(premium_plan=self.premium_plan_2)
        self.normal_user4 = NormalUserFactory(premium_plan=self.premium_plan_2)

        self.client.force_authenticate(user=self.super_admin)

        self.url_name = "normal-user"

    def test_list(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 4)
    
    def test_list_with_email_filter(self):
        response = self.client.get(reverse(self.url_name) + "?email=" + self.normal_user1.email)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["first_name"], self.normal_user1.first_name)
    
    def test_list_with_created_at_filter(self):
        start_date = datetime.today()
        end_date = datetime.today()
        response = self.client.get(reverse(self.url_name) + "?created_at_after=" 
                    + str(start_date)
                    + "&created_at_before="
                    + str(end_date))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)

    def test_list_with_name_filter(self):
        base_url = reverse(self.url_name) + "?name="
        def test_res(url: str, equal_to: str):
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["count"], 1)
            self.assertEqual(response.data["results"][0]["first_name"], equal_to)
        
        url = base_url + self.normal_user2.first_name
        test_res(url, self.normal_user2.first_name)

        url = base_url + self.normal_user3.last_name
        test_res(url, self.normal_user3.first_name)

        url = base_url + self.normal_user4.first_name + " " + self.normal_user4.last_name
        test_res(url, self.normal_user4.first_name)
    
    def test_list_ordering(self):
        test_ordering(self, self.ordering_fields, self.url_name)
