import unittest
from moodscores import custom_vader

class TestVader(unittest.TestCase):

    def setUp(self):
        self.vader = custom_vader.SentimentIntensityAnalyzer()
        self.Anew_Dominance_vader = custom_vader.SentimentIntensityAnalyzer(lexicon = 'ANEW_Dominance')
        self.tweet = 'I love using this package because it is so fun :)'

    def test_Vader_scoring(self):
        self.assertEqual( self.vader.polarity_scores(self.tweet)[0], {'neg': 0.0, 'neu': 0.374, 'pos': 0.626, 'compound': 0.9139})

    def test_Vader_tokens(self):
    	self.assertEqual( self.vader.polarity_scores(self.tweet)[1], ['love', 'fun', ':)'])

    def test_CVader_scoring(self):
        self.assertEqual( self.Anew_Dominance_vader.polarity_scores(self.tweet)[0], {'neg': 0.0, 'neu': 0.231, 'pos': 0.769, 'compound': 0.9822})

    def test_CVader_tokens(self):
    	self.assertEqual( self.Anew_Dominance_vader.polarity_scores(self.tweet)[1], ['love', 'package', 'fun'])
