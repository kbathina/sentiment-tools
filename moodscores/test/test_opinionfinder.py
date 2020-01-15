import unittest
from moodscores import opinionfinder

class TestOpinionFinder(unittest.TestCase):

    def setUp(self):
        self.OF = opinionfinder.OpinionFinder()
        self.tweet = 'I love using this package because it is so fun'

    def test_sum(self):
        self.assertEqual( self.OF.Score(self.tweet,'Sum')[0], 2.0)

    def test_average(self):
        self.assertEqual( self.OF.Score(self.tweet,'Average')[0], 0.6666666666666666)

    def test_tokens(self):
    	self.assertEqual( self.OF.Score(self.tweet,'Sum')[1], ['love', 'so', 'fun'])