from django.test import TestCase
from http import HTTPStatus

# Create your tests here.

class RobotsTest(TestCase):
    def test_get(self):
        response = self.client.get("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], "User-Agent: *")

    def test_post(self):
        response = self.client.post("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)


class DnsTest(TestCase):
    def test_get(self):
        response = self.client.get("/dns.txt")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], "User-Agent: *")

    def test_post(self):
        response = self.client.post("/dns.txt")

        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)