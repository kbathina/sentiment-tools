import unittest
from moodscores import gpoms

class TestGPOMS(unittest.TestCase):

    def setUp(self):
        self.gpoms = gpoms.GPOMS()
        self.tweet = 'I love using this package because it is so fun'

    def test_sum(self):
        self.assertEqual( self.gpoms.Score(self.tweet,'Sum')[0], {'composed/anxious': 0.13699999999999998, 'agreeable/hostile': 0.74, 'elated/depressed': 0.07700000000000001, 'confident/unsure': 0.183, 'clearheaded/confused': -0.046, 'energetic/tired': 0.45899999999999996})

    def test_average(self):
        self.assertEqual( self.gpoms.Score(self.tweet,'Average')[0], {'composed/anxious': 0.13699999999999998, 'agreeable/hostile': 0.37, 'elated/depressed': 0.038500000000000006, 'confident/unsure': 0.0915, 'clearheaded/confused': -0.023, 'energetic/tired': 0.22949999999999998})

    def test_tokens(self):
    	self.assertEqual( self.gpoms.Score(self.tweet,'Sum')[1], {'composed/anxious': ['fun'], 'agreeable/hostile': ['love', 'fun'], 'elated/depressed': ['love', 'fun'], 'confident/unsure': ['love', 'fun'], 'clearheaded/confused': ['love', 'fun'], 'energetic/tired': ['love', 'fun']})