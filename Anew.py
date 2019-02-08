import numpy as np
import pandas as pd
import re

class Anew(object):

    def __init__(self):

        self.words, self.Arousal, self.Dominance, self.Valence = self.Setup()
        self.punc_replace = lambda x: re.sub(r'[^\w\s]','',x)

    def Setup(self):

        with open('sentiment_tools/data/Anew_arousal.txt') as f:
            Arousal = [x.strip().split('\t') for x in f.readlines()]
            Arousal = {x:float(y) for x,y in Arousal}

        with open('sentiment_tools/data/Anew_dominance.txt') as f:
            Dominance = [x.strip().split('\t') for x in f.readlines()]
            Dominance = {x:float(y) for x,y in Dominance}

        with open('sentiment_tools/data/Anew_valence.txt') as f:
            Valence = [x.strip().split('\t') for x in f.readlines()]
            Valence = {x:float(y) for x,y in Valence}

        words = Arousal.keys()

        return words, Arousal, Dominance, Valence

    def Score(self,tweet, return_type):
        total = 0
        results = {'Valence':0, 'Arousal':0, 'Dominance':0}
        tweet = self.punc_replace(tweet).lower().split(' ')

        for word in tweet:
            if word in self.words:
                total += 1
                results['Valence'] += self.Valence[word]
                results['Arousal'] += self.Arousal[word]
                results['Dominance'] += self.Dominance[word]

        if total == 0: return {'Valence':None, 'Arousal':None, 'Dominance':None}

        if return_type == 'Sum': return results
        elif return_type == 'Average':
            results['Valence'] = results['Valence'] / total
            results['Arousal'] = results['Arousal'] / total
            results['Dominance'] = results['Dominance'] / total
            return results

