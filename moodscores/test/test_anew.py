import unittest
from moodscores import anew

class TestAnew(unittest.TestCase):

    def setUp(self):
        self.anew = anew.Anew()
        self.tweet = 'I love using this package because it is so fun'

    def test_sum(self):
        self.assertEqual( self.anew.Score(self.tweet,'Sum')[0], {'Valence': 21.54, 'Arousal': 16.41, 'Dominance': 18.13})

    def test_average(self):
        self.assertEqual( self.anew.Score(self.tweet,'Average')[0], {'Valence': 7.18, 'Arousal': 5.47, 'Dominance': 6.043333333333333})

    def test_tokens(self):
    	self.assertEqual( self.anew.Score(self.tweet,'Sum')[1], ['love', 'package', 'fun'])