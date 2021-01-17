from django.test import TestCase, Client


class LoginTest(TestCase):
    """
    Test module for Login
    """
    def setUp(self):
        self.base_url = 'http://0.0.0.0:3000/api/users/login/'
        self.client = Client()

    def test_login(self):
        """ Test Login """
        response = self.client.get(self.base_url)
        # Test success listing
        self.assertEqual(response.status_code, 200)


class RegisterTest(TestCase):
    """
    Test module for Register
    """
    def setUp(self):
        self.base_url = 'http://0.0.0.0:3000/api/users/register/'
        self.client = Client()

    def test_register(self):
        """ Test Register """
        response = self.client.get(self.base_url)
        # Test success listing
        self.assertEqual(response.status_code, 200)
