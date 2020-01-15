import unittest
from moodscores import afinn

class TestAfinn(unittest.TestCase):

    def setUp(self):
        self.afinn = afinn.Afinn()
        self.tweet = 'I love using this package because it is so fun'

    def test_sum(self):
        self.assertEqual( self.afinn.Score(self.tweet,'Sum')[0], 7)

    def test_average(self):
        self.assertEqual( self.afinn.Score(self.tweet,'Average')[0], 3.5)

    def test_tokens(self):
    	self.assertEqual( self.afinn.Score(self.tweet,'Sum')[1], ['love', 'fun'])