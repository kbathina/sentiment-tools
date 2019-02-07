import numpy as np
import pandas as pd

class Anew(object):

    def __init__(self):

        self.norms = self.Setup()

    def Setup(self):
        norms = pd.read_csv('sentiment_tools/norm_warriner.csv')
        norms.index = norms.Word
        norms = norms[['V.Mean.Sum','V.SD.Sum','A.Mean.Sum','A.SD.Sum','D.Mean.Sum','D.SD.Sum']]
        columns = ['V_Mean', 'V_SD','A_Mean','A_SD','D_Mean','D_SD']
        norms.columns = ['V_Mean', 'V_SD','A_Mean','A_SD','D_Mean','D_SD']
        norms_dict = dict([(i,np.array([a,b,c])) for i, a,b,c in zip(norms.index.tolist(), norms.V_Mean, norms.A_Mean, norms.D_Mean)])

        return norms_dict

    def Score(self,tweet, return_type): # for average, only counts words if it exists norms
        total = 0
        results = {'Valence':0, 'Arousal':0, 'Dominance':0}
        for word in tweet.lower().split(' '):
            if word in self.norms:
                total += 1
                results['Valence'] += self.norms[word][0]
                results['Arousal'] += self.norms[word][1]
                results['Dominance'] += self.norms[word][2]

        if return_type == 'Sum': return results
        elif return_type == 'Average':
            if total:
                results['Valence'] = results['Valence'] / total
                results['Arousal'] = results['Arousal'] / total
                results['Dominance'] = results['Dominance'] / total
                return results
            else:
                return results
