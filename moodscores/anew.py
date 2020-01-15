import numpy as np
import pandas as pd
from moodscores.helper_functions import tokenizer
from moodscores import _ROOT,get_data

AROUSAL_DATA = get_data('Anew_arousal.txt')
VALENCE_DATA = get_data('Anew_valence.txt')
DOMINANCE_DATA = get_data('Anew_dominance.txt')

class Anew(object):

    def __init__(self):

        self.words, self.Arousal, self.Dominance, self.Valence = self.Setup()

    def Setup(self):

        with open(AROUSAL_DATA) as f:
            Arousal = [x.strip().split('\t') for x in f.readlines()]
            Arousal = {x:float(y) for x,y in Arousal}

        with open(DOMINANCE_DATA) as f:
            Dominance = [x.strip().split('\t') for x in f.readlines()]
            Dominance = {x:float(y) for x,y in Dominance}

        with open(VALENCE_DATA) as f:
            Valence = [x.strip().split('\t') for x in f.readlines()]
            Valence = {x:float(y) for x,y in Valence}

        words = Arousal.keys()

        return words, Arousal, Dominance, Valence

    def Score(self,tweet, calculation_type):

        if calculation_type != 'Sum' and calculation_type != 'Average':
            raise ValueError("calculation_type return be 'Sum' or 'Average'")

        total = 0
        results = {'Valence':0, 'Arousal':0, 'Dominance':0}
        tokenized_list = tokenizer(tweet)
        tokens_in_wordlist = []

        for word in tokenized_list:
            if word in self.words:
                tokens_in_wordlist.append(word)
                total += 1
                results['Valence'] += self.Valence[word]
                results['Arousal'] += self.Arousal[word]
                results['Dominance'] += self.Dominance[word]

        if total == 0: return [{'Valence':None, 'Arousal':None, 'Dominance':None}, tokens_in_wordlist]

        if calculation_type == 'Sum': return [results, tokens_in_wordlist]
        elif calculation_type == 'Average':
            results['Valence'] = results['Valence'] / total
            results['Arousal'] = results['Arousal'] / total
            results['Dominance'] = results['Dominance'] / total
            return [results, tokens_in_wordlist]

