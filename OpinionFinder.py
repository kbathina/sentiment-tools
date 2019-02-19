import numpy as np
import re

class OpinionFinder(object):

    def __init__(self):
        self.OP = self.Setup()

    def Setup(self):
        with open('sentiment_tools/data/OpFi-Sent.txt','r') as f:
            OP = f.readlines()
            OP = [x.strip().split(' ') for x in OP]
            OP = {x:np.sign(float(y)) for x,y in OP}

        return OP

    def punc_replace(self,tweet):
        return re.sub(r'[^\w\s]','',tweet)

    def Score(self,tweet, return_type):
        total = 0
        sent = 0
        tokenized_list = self.punc_replace(tweet).lower().split(' ')
        tokens_in_wordlist = []

        for word in tokenized_list:
            if word in self.OP:
                tokens_in_wordlist.append(word)
                total += 1
                sent += self.OP[word]  

        if total == 0: return [None, tokens_in_wordlist]
        else: 
            if return_type == 'Sum': return [sent, tokens_in_wordlist]
            elif return_type ==	 'Average': return [sent/total, tokens_in_wordlist]
