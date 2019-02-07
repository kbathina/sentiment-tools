import numpy as np
import pandas as pd

class Pom(object):

    def __init__(self):

        self.poms = self.Setup()

    def Setup(self):
        poms = pd.read_csv('sentiment_tools/data/POMS.csv', sep = '\t', index_col='Word')
        columns = ['composed/anxious', 'agreeable/hostile','elated/depressed',
        'confident/unsure', 'clearheaded/confused', 'energetic/tired']
        poms_dict = dict([(i,np.array([a,b,c,d,e,f])) for i, a,b,c,d,e,f in 
            zip(poms.index.tolist(), poms['composed/anxious'], poms['agreeable/hostile'], 
                poms['elated/depressed'], poms['confident/unsure'], 
                poms['clearheaded/confused'], poms['energetic/tired'])])

        return poms_dict

    def Score(self,tweet, return_type):
        total = 0
        results = {'composed/anxious':0, 
        'agreeable/hostile':0, 
        'elated/depressed':0,
        'confident/unsure':0,
        'clearheaded/confused':0,
        'energetic/tired':0}

        for word in tweet.lower().split(' '):
            if word in self.poms:
                total += 1
                results['composed/anxious'] += self.poms[word][0]
                results['agreeable/hostile'] += self.poms[word][1]
                results['elated/depressed'] += self.poms[word][2]
                results['confident/unsure'] += self.poms[word][3]
                results['clearheaded/confused'] += self.poms[word][4]
                results['energetic/tired'] += self.poms[word][5]

        if total == 0: 
            return  {'composed/anxious': None, 'agreeable/hostile': None, 
            'elated/depressed': None, 'confident/unsure': None, 
            'clearheaded/confused': None, 'energetic/tired': None}

        if return_type == 'Sum': return results
        elif return_type == 'Average':
            results['composed/anxious'] = results['composed/anxious'] / total
            results['agreeable/hostile'] = results['agreeable/hostile'] / total
            results['elated/depressed'] = results['elated/depressed']  / total
            results['confident/unsure'] = results['confident/unsure']  / total
            results['clearheaded/confused'] = results['clearheaded/confused']  / total
            results['energetic/tired'] = results['energetic/tired']  / total
            return results



