import numpy as np
import pandas as pd
from moodscores.helper_functions import tokenizer
from moodscores import _ROOT,get_data

GPOMS_DATA = get_data('GPOMS.csv')


class GPOMS(object):

    def __init__(self):

        self.gpoms = self.Setup()

    def Setup(self):

        gpoms = pd.read_csv(GPOMS_DATA, sep = '\t', index_col='Word')
        gpoms = gpoms.replace({0: None})

        columns = ['composed/anxious', 'agreeable/hostile','elated/depressed',
        'confident/unsure', 'clearheaded/confused', 'energetic/tired']
        gpoms_dict = dict([(i,np.array([a,b,c,d,e,f])) for i, a,b,c,d,e,f in 
            zip(gpoms.index.tolist(), gpoms['composed/anxious'], gpoms['agreeable/hostile'], 
                gpoms['elated/depressed'], gpoms['confident/unsure'], 
                gpoms['clearheaded/confused'], gpoms['energetic/tired'])])

        return gpoms_dict

    def Score(self,tweet, calculation_type):

        if calculation_type != 'Sum' and calculation_type != 'Average':
            raise ValueError("calculation_type return be 'Sum' or 'Average'")


        total = 0
        results = {'composed/anxious':0, 
        'agreeable/hostile':0, 
        'elated/depressed':0,
        'confident/unsure':0,
        'clearheaded/confused':0,
        'energetic/tired':0}

        tokenized_list = tokenizer(tweet)
        tokens_in_wordlist = {'composed/anxious':[],'agreeable/hostile':[],
        'elated/depressed':[],'confident/unsure':[],'clearheaded/confused':[],'energetic/tired':[]}
        totals = {'composed/anxious':0,'agreeable/hostile':0,
        'elated/depressed':0,'confident/unsure':0,'clearheaded/confused':0,'energetic/tired':0}

        for word in tokenized_list:
            if word in self.gpoms:
                if type(self.gpoms[word][0]) != type(None):
                    results['composed/anxious'] += self.gpoms[word][0]
                    tokens_in_wordlist['composed/anxious'].append(word)
                    totals['composed/anxious'] += 1
                if type(self.gpoms[word][1]) != type(None):
                    results['agreeable/hostile'] += self.gpoms[word][1]
                    tokens_in_wordlist['agreeable/hostile'].append(word)
                    totals['agreeable/hostile'] += 1
                if type(self.gpoms[word][2]) != type(None):
                    results['elated/depressed'] += self.gpoms[word][2]
                    tokens_in_wordlist['elated/depressed'].append(word)
                    totals['elated/depressed'] += 1                    
                if type(self.gpoms[word][3]) != type(None):
                    results['confident/unsure'] += self.gpoms[word][3]
                    tokens_in_wordlist['confident/unsure'].append(word)
                    totals['confident/unsure'] += 1                    
                if type(self.gpoms[word][4]) != type(None):
                    results['clearheaded/confused'] += self.gpoms[word][4]
                    tokens_in_wordlist['clearheaded/confused'].append(word)
                    totals['clearheaded/confused'] += 1                    
                if type(self.gpoms[word][5]) != type(None):
                    results['energetic/tired'] += self.gpoms[word][5]
                    tokens_in_wordlist['energetic/tired'].append(word)
                    totals['energetic/tired'] += 1                    

        if calculation_type == 'Sum': return [results, tokens_in_wordlist]
        elif calculation_type == 'Average':
            if totals['composed/anxious'] > 0:
                results['composed/anxious'] /= totals['composed/anxious']
            if totals['agreeable/hostile'] > 0:
                results['agreeable/hostile'] /= totals['agreeable/hostile']
            if totals['elated/depressed'] > 0:
                results['elated/depressed']  /= totals['elated/depressed']
            if totals['confident/unsure'] > 0:
                results['confident/unsure']  /= totals['confident/unsure']
            if totals['clearheaded/confused'] > 0:
                results['clearheaded/confused']  /= totals['clearheaded/confused']
            if totals['energetic/tired'] > 0:
                results['energetic/tired']  /= totals['energetic/tired']

            return [results, tokens_in_wordlist]



