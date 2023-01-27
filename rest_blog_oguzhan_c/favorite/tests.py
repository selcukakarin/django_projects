from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.utils import json

from favorite.models import Favorite
from post.models import Post


class FavoriteCreateList(APITestCase):
    url = reverse("favorite:list-create")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "selcuk"
        self.password = "Microman1903"
        self.post = Post.objects.create(title="Başlık", content="İçerik")
        self.user = User.objects.create_user(username=self.username,
                                             password=self.password)
        self.test_jwt_authentication()

    def test_jwt_authentication(self):
        response = self.client.post(self.url_login,
                                    data={"username": self.username,
                                          "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    ## buranın çalışması için settingsden token ayarları açılmalı
    # favlama
    def test_add_favorite(self):
        data = {
            "content": "içerik güzell",
            "user": self.user.id,
            "post": self.post.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    # listeleme
    def test_user_favs(self):
        self.test_add_favorite()
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)[
                                "results"]) == Favorite.objects.filter(
            user=self.user).count())


class FavoriteUpdateDeleteTest(APITestCase):
    login_url = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "selcuk"
        self.password = "Microman1903"
        self.user = User.objects.create_user(username=self.username,
                                             password=self.password)
        self.user2 = User.objects.create_user(username="selcuk2",
                                              password=self.password)
        self.post = Post.objects.create(title="Başlık", content="İçerik")
        self.favorite = Favorite.objects.create(content="deneme",
                                                post=self.post,
                                                user=self.user)
        self.url = reverse("favorite:delete-retrieve",
                           kwargs={"pk": self.favorite.pk})
        self.url2 = reverse("favorite:update-retrieve",
                            kwargs={"pk": self.favorite.pk})
        self.test_jwt_authentication()

    def test_jwt_authentication(self, username="selcuk",
                                password="Microman1903"):
        response = self.client.post(self.login_url,
                                    data={"username": self.username,
                                          "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    # silme islemi
    def test_fav_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)

    ## buranın çalışması için settingsden token ayarları kapatilmali
    def test_fav_delete_different_user(self):
        self.test_jwt_authentication("selcuk2")
        response = self.client.delete(self.url)
        self.assertEqual(403, response.status_code)

    ## buranın çalışması için settingsden token ayarları acilmali
    # düzenleme işlemi
    def test_fav_update(self):
        data = {
            "content": "içerik 123",
            "post": self.post.id,
            "user": self.user.id
        }
        response = self.client.put(self.url2, data)
        self.assertEqual(200, response.status_code)
        self.assertTrue(Favorite.objects.get(id=self.favorite.id).content == data["content"])

    # baskasi benim adima islem yaparsa
    def test_fav_update_different_user(self):
        self.test_jwt_authentication("selcuk233")
        data = {
            "content": "içerik 123",
            "user": self.user2.id
        }
        response = self.client.put(self.url, data)
        self.assertTrue(403, response.status_code)

    # giris yapmadan link görülemez.
    def test_unauthorization(self):
        self.client.credentials() ## bu sekilde oturum sonlandirilmis olur
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)