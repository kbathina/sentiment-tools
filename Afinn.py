import afinn
import numpy as np

class Afinn(object):

    def __init__(self):
        self.afinn = afinn.Afinn()
    def Score(self,tweet, return_type): # for average, only counts words if it exists norms
        
        tweet_lower = tweet.lower()
        score=self.afinn.score(tweet_lower)
        tokens_in_wordlist = self.afinn.find_all(tweet_lower)
        total = len(tokens_in_wordlist)

        if total == 0: return [None, tokens_in_wordlist]
        else: 
            if return_type == 'Sum': return [score, tokens_in_wordlist]
            elif return_type ==	 'Average': return [score/total, tokens_in_wordlist]
