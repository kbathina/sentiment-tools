import afinn
import numpy as np

class Afinn(object):

    def __init__(self):
        self.afinn = afinn.Afinn()
    def Score(self,tweet, return_type): # for average, only counts words if it exists norms
        
        scores=self.afinn.scores(tweet.lower())
        total = len(scores)

        if total == 0:
            return 0
        else: 
            if return_type == 'Sum': return sum(scores)
            elif return_type ==	 'Average': return sum(scores) / total
