from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
"""
class HomePageViewTest(TestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageViewTest(TestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200) 
"""
class PostTes(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
    
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get("home")
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get("home")
        self.assertEqual(response, "pages/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")