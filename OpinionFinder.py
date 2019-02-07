import numpy as np

class OpinionFinder(object):

    def __init__(self):
        self.OP = self.Setup()

    def Setup(self):
        with open('sentiment_tools/data/OpFi-Sent.txt','r') as f:
            OP = f.readlines()
            OP = [x.strip().split(' ') for x in OP]
            OP = {x:np.sign(float(y)) for x,y in OP}

        return OP

    def Score(self,tweet, return_type):
        total = 0
        sent = 0
        for word in tweet.lower().split(' '):
            if word in self.OP:
                total += 1
                sent += self.OP[word]  

        if total == 0: return None
        else: 
            if return_type == 'Sum': return sent
            elif return_type ==	 'Average': return sent/total 
