from django.test import TestCase
from django.urls import reverse
from .models import Match

class MatchTests(TestCase):

    def setUp(self):
        self.match = Match.objects.create(
            match_date='2021-08-21',
            home_team='testTeam',
            home_score='10',
            away_team='testOpps',
            away_score='5',
            match_report='This is a test report.'
        )

    def test_match_post(self):
        self.assertEqual(f'{self.match.match_date}', '2021-08-21')
        self.assertEqual(f'{self.match.home_team}', 'testTeam')
        self.assertEqual(f'{self.match.home_score}', '10')
        self.assertEqual(f'{self.match.away_team}', 'testOpps')
        self.assertEqual(f'{self.match.away_score}', '5')
        self.assertEqual(f'{self.match.match_report}', 'This is a test report.')