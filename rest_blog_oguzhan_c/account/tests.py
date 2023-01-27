from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.utils import json


# dogru veilerle kayıt islemi
# sifre invalid olabilir
# kullanıcı adı kullanılmıs olabilir
# uye girisi yaptıysak register sayfası gozukmemeli
# token ile giris islemi yapıldıgında 403 hatası donmeli

class UserRegistrationTestCase(APITestCase):
    url = reverse("account:register")
    url_login = reverse("token_obtain_pair")

    def test_user_registration(self):
        """
            dogru veriler ile kayit islemi
        """

        data = {
            "username": "selcuktest1",
            "email": "selcuktest@gmail.com",
            "password": "deneme1SSS"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_user_invalid_password(self):
        """
            invalid password  ile kayit
        """

        data = {
            "username": "selcuktest1",
            "email": "selcuktest@gmail.com",
            "password": "1"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_unique_name(self):
        """
            benzersiz isim testi
        """

        self.test_user_registration()  # user register oldu
        data = {
            "username": "selcuktest1",
            "email": "selcuktest@gmail.com",
            "password": "deneme1SSS"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_user_authenticated_registration(self):
        """
            session ile giris yapmıs kullanici sayfayi görememeli

            burayi calistirmak icin settingsteki REST_FRAMEWORK ayarlarini kapa. JWTAuthentication isi bozuyor
        """

        self.test_user_registration()  # user register oldu
        self.client.login(username='selcuktest1', password='deneme1SSS')
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    def test_user_authenticated_token(self):
        """
            token ile giris yapmıs kullanici sayfayi görememeli
            burayi calistirmak icin settingsteki REST_FRAMEWORK ayarlarini ac. JWTAuthentication olmasi gerek
        """

        self.test_user_registration()  # user register oldu
        data = {
            "username": "selcuktest1",
            "email": "selcuktest@gmail.com",
            "password": "deneme1SSS"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_2 = self.client.get(self.url)
        self.assertEqual(403, response_2.status_code)


class UserLogin(APITestCase):
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "selcuk"
        self.password = "Microman1903"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_user_token(self):
        response = self.client.post(self.url_login, {"username": "selcuk", "password": "Microman1903"})
        self.assertEqual(200, response.status_code)
        print(json.loads(response.content))
        self.assertTrue("access" in json.loads(response.content))

    def test_user_invalid_data(self):
        response = self.client.post(self.url_login, {"username": "selcuk21312", "password": "Microman1903"})
        self.assertEqual(401, response.status_code)

    def test_user_empty_data(self):
        response = self.client.post(self.url_login, {"username": "", "password": ""})
        self.assertEqual(400, response.status_code)

    # 429 too many request
    # 400 login data empty
    # 200 succesfull
    # 401 invalid user
    # 403 already registered


class UserPasswordChange(APITestCase):
    # oturum acilmadan girildiginde hata
    url = reverse("account:change-password")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "selcuk"
        self.password = "Microman1903"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def login_with_token(self):
        data = {
            "username": "selcuk",
            "password": "Microman1903"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_is_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_with_valid_information(self):
        self.login_with_token()
        data = {
            "old_password": "Microman1903",
            "new_password": "asfasfasSAas212"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(204, response.status_code)

    def test_with_wrong_information(self):
        self.login_with_token()
        data = {
            "old_password": "Micromasfasan1903",
            "new_password": "asfasfasSAsadsaas212"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_with_empty_information(self):
        self.login_with_token()
        data = {
            "old_password": "",
            "new_password": ""
        }
        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)


class UserProfileUpdate(APITestCase):
    url = reverse("account:me")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "selcuk"
        self.password = "Microman1903"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def login_with_token(self):
        data = {
            "username": "selcuk",
            "password": "Microman1903"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    # oturum acilmadan girildiginde hata
    def test_is_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    # valid information
    def test_with_valid_information(self):
        self.login_with_token()
        data = {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "profile": {
                "id": 1,
                "note": "sadasd",
                "twitter": "sadasdas"
            }
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content), data)

    def test_user_empty_data(self):
        self.login_with_token()
        data = {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "profile": {
                "id": 1,
                "note": "",
                "twitter": ""
            }
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(400, response.status_code)
