import numpy as np
from moodscores.helper_functions import tokenizer
from moodscores import _ROOT,get_data

OF_DATA = get_data('OpFi-Sent.txt')

class OpinionFinder(object):

    def __init__(self):
        self.OP = self.Setup()

    def Setup(self):
        with open(OF_DATA,'r') as f:
            OP = f.readlines()
            OP = [x.strip().split(' ') for x in OP]
            OP = {x:np.sign(float(y)) for x,y in OP}

        return OP

    def Score(self,tweet, calculation_type):

        if calculation_type != 'Sum' and calculation_type != 'Average':
            raise ValueError("calculation_type return be 'Sum' or 'Average'")
            
        total = 0
        sent = 0
        tokenized_list = tokenizer(tweet)
        tokens_in_wordlist = []

        for word in tokenized_list:
            if word in self.OP:
                tokens_in_wordlist.append(word)
                total += 1
                sent += self.OP[word]  

        if total == 0: return [None, tokens_in_wordlist]
        else: 
            if calculation_type == 'Sum': return [sent, tokens_in_wordlist]
            elif calculation_type =='Average': return [sent/total, tokens_in_wordlist]
