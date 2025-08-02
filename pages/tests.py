from django.test import TestCase

# Create your tests here.
class HomePageViewTest(TestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageViewTest(TestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200) 