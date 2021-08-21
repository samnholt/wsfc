from django.test import SimpleTestCase
from .views import HomePageView, AboutPageView, StatsPageView
from django.urls import reverse, resolve

# Tests for Home Page
class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'ESTABLISHED 2020')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response,
            'Hi there! I am an evil dragon. I should not be on the page')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
            )

# About page tests

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_correct_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'Club Information')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response,
            'I am another evil dragon. Please do not allow me on page')

    def test_aboutpage_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__,
            AboutPageView.as_view().__name__)

class StatsPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('stats')
        self.response = self.client.get(url)

    def test_stats_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_statspage_correct_template(self):
        self.assertTemplateUsed(self.response, 'stats.html')

    def test_statspage_contains_correct_html(self):
        self.assertContains(self.response, 'Match & Player Statistics')

    def test_statspage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response,
            'I am another evil dragon. Please do not allow me on page')

    def test_statspage_resolves_statspageview(self):
        view = resolve('/stats/')
        self.assertEqual(view.func.__name__,
            StatsPageView.as_view().__name__)