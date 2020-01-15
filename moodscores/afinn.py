import afinn
import numpy as np

class Afinn(object):


    def __init__(self):
        """
        initilization of class
        initializes Afinn
        """

        self.afinn = afinn.Afinn()


    def Score(self,tweet, calculation_type): 
        """
        Scoring function
        Takes "Sum" or "Average" as input for return type
        """
        if calculation_type != 'Sum' and calculation_type != 'Average':
            raise ValueError("calculation_type return be 'Sum' or 'Average'")
        
        tweet_lower = tweet.lower() # lowercase the tweet
        score=self.afinn.score(tweet_lower) # find score of tweet
        tokens_in_wordlist = self.afinn.find_all(tweet_lower) # get list of tokens
        total = len(tokens_in_wordlist) # get lenngth of tokens

        # if no tokens: return none and empty token list
        if total == 0: return [None, tokens_in_wordlist]
        else: 
            # if sum, return score and token list
            if calculation_type == 'Sum': return [score, tokens_in_wordlist]
            # if average, divide score with number of tokenns
            # return average and token list
            elif calculation_type == 'Average': return [score/total, tokens_in_wordlist]
