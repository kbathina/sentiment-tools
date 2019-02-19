import numpy as np
import pandas as pd
import re

class GPOMS(object):

    def __init__(self):

        self.gpoms = self.Setup()

    def Setup(self):
        gpoms = pd.read_csv('sentiment_tools/data/GPOMS.csv', sep = '\t', index_col='Word')
        columns = ['composed/anxious', 'agreeable/hostile','elated/depressed',
        'confident/unsure', 'clearheaded/confused', 'energetic/tired']
        gpoms_dict = dict([(i,np.array([a,b,c,d,e,f])) for i, a,b,c,d,e,f in 
            zip(gpoms.index.tolist(), gpoms['composed/anxious'], gpoms['agreeable/hostile'], 
                gpoms['elated/depressed'], gpoms['confident/unsure'], 
                gpoms['clearheaded/confused'], gpoms['energetic/tired'])])

        return gpoms_dict

    def punc_replace(self,tweet):
        return re.sub(r'[^\w\s]','',tweet)

    def Score(self,tweet, return_type):
        total = 0
        results = {'composed/anxious':0, 
        'agreeable/hostile':0, 
        'elated/depressed':0,
        'confident/unsure':0,
        'clearheaded/confused':0,
        'energetic/tired':0}

        tokenized_list = self.punc_replace(tweet).lower().split(' ')
        tokens_in_wordlist = []
        for word in tokenized_list:
            if word in self.gpoms:
                tokens_in_wordlist.append(word)
                total += 1
                results['composed/anxious'] += self.gpoms[word][0]
                results['agreeable/hostile'] += self.gpoms[word][1]
                results['elated/depressed'] += self.gpoms[word][2]
                results['confident/unsure'] += self.gpoms[word][3]
                results['clearheaded/confused'] += self.gpoms[word][4]
                results['energetic/tired'] += self.gpoms[word][5]

        if total == 0: 
            return  [{'composed/anxious': None, 'agreeable/hostile': None, 
            'elated/depressed': None, 'confident/unsure': None, 
            'clearheaded/confused': None, 'energetic/tired': None}, tokens_in_wordlist]

        if return_type == 'Sum': return [results, tokens_in_wordlist]
        elif return_type == 'Average':
            results['composed/anxious'] = results['composed/anxious'] / total
            results['agreeable/hostile'] = results['agreeable/hostile'] / total
            results['elated/depressed'] = results['elated/depressed']  / total
            results['confident/unsure'] = results['confident/unsure']  / total
            results['clearheaded/confused'] = results['clearheaded/confused']  / total
            results['energetic/tired'] = results['energetic/tired']  / total
            return [results, tokens_in_wordlist]



