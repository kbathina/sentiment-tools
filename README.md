# How to use

## Some techniques have two possible methods. 'Sum' finds the sum of the values per tweet while 'Average' finds the mean value per tweet. Only words with a score are counted.

## Returns scores (by dimension if necessary) and tokenized list of words in the dictionary
## NA means no words were matched

```python
import sentiment_tools
tweet = 'The best thing about this package is how easy it is to use!!'
```

## Opinion Finder

```python
OF = sentiment_tools.OpinionFinder.OpinionFinder()

sentiment_sum,tokenized_list_of_words_sum = OF.Score(tweet,'Sum')
sentiment_ave,tokenized_list_of_words_ave = OF.Score(tweet,'Average')

print('OpinionFinder Sum =', sentiment_sum)
```
OpinionFinder Sum = 2.0
```python
print('Tokenized list (from Sum) =', tokenized_list_of_words_sum)
```
Tokenized list (from Sum) = ['best', 'easy']
```python
print('OpinionFinder Average =', sentiment_ave)
```
OpinionFinder Average = 1.0
```python
print('Tokenized list (from Average) =', tokenized_list_of_words_ave)
```
Tokenized list (from Average) = ['best', 'easy']


## Vader

```python
vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer()

sentiment_vader, tokenized_list_of_words_vader = vader.polarity_scores(tweet)
print('Vader Scoring Dimensions =', list(sentiment_vader.keys()))
```
Vader Scoring Dimensions = ['neu', 'neg', 'compound', 'pos']
```python
for dimension in sentiment_vader.keys():
	 	print(dimension + ' score =', sentiment_vader[dimension])
```
neu score = 0.589  
neg score = 0.0  
compound score = 0.8264  
pos score = 0.411  
```python
print('Tokenized list =', tokenized_list_of_words_vader)
```
Tokenized list = ['The', 'best', 'thing', 'about', 'this', 'package', 'is', 'how', 'easy', 'it', 'is', 'to', 'use']


## Vader with Opinion Finder

```python
OF_Vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/data/OpFi-Sent.txt', lex_sep= ' ')

sentiment_vader, tokenized_list_of_words_vader = OF_Vader.polarity_scores(tweet)
for dimension in sentiment_vader.keys():
	print(dimension + ' score =', sentiment_vader[dimension])
```
neu score = 0.729  
neg score = 0.0  
compound score = 0.4738  
pos score = 0.271  
```python
print('Tokenized list =', tokenized_list_of_words_vader)
```
Tokenized list = ['The', 'best', 'thing', 'about', 'this', 'package', 'is', 'how', 'easy', 'it', 'is', 'to', 'use']

## ANEW

```python
ANEW = sentiment_tools.Anew.Anew()

sentiment_sum,tokenized_list_of_words_sum = ANEW.Score(tweet,'Sum')
sentiment_ave,tokenized_list_of_words_ave = ANEW.Score(tweet,'Average')

print('ANEW Scoring Dimensions =', list(sentiment_sum.keys()))
```
ANEW Scoring Dimensions = ['Arousal', 'Valence', 'Dominance']
```python
for dimension in sentiment_sum.keys():
	print(dimension + ' score (Sum) =', sentiment_sum[dimension])
	print(dimension + ' score (Average) =', sentiment_ave[dimension])
```
Arousal score (Sum) = 16.17  
Arousal score (Average) = 4.0425  
Valence score (Sum) = 23.369999999999997  
Valence score (Average) = 5.842499999999999  
Dominance score (Sum) = 22.37  
Dominance score (Average) = 5.5925  
```python
print(tokenized_list_of_words_sum)
print(tokenized_list_of_words_sum == tokenized_list_of_words_ave)
```
['thing', 'package', 'easy', 'use']  
True


## Vader with Anew

```python
arousal_vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/data/Anew_arousal.txt', lex_sep= '\t')
valence_vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/data/Anew_valence.txt', lex_sep= '\t')
dominance_vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/data/Anew_dominance.txt', lex_sep= '\t')

a_sentiment, a_tokens = arousal_vader.polarity_scores(tweet)
v_sentiment, v_tokens = valence_vader.polarity_scores(tweet)
d_sentiment, d_tokens = dominance_vader.polarity_scores(tweet)

for dimension in a_sentiment.keys():
	print('Arousal score ' + dimension + ' =', a_sentiment[dimension])
	print('Valence score ' + dimension + ' =', v_sentiment[dimension])
	print('Dominance score ' + dimension + ' =', d_sentiment[dimension])
```
Arousal score neu = 0.302  
Valence score neu = 0.244  
Dominance score neu = 0.25  
Arousal score neg = 0.0  
Valence score neg = 0.0  
Dominance score neg = 0.0  
Arousal score compound = 0.9743  
Valence score compound = 0.9872  
Dominance score compound = 0.9861  
Arousal score pos = 0.698  
Valence score pos = 0.756  
Dominance score pos = 0.75  
```python
print(a_tokens)
print(a_tokens == v_tokens == d_tokens)
```
['The', 'best', 'thing', 'about', 'this', 'package', 'is', 'how', 'easy', 'it', 'is', 'to', 'use']  
True

## Afinn

```python
afinn = sentiment_tools.Afinn.Afinn()

sentiment_afinn_sum, tokens_afinn_sum = afinn.Score(tweet,'Sum')
sentiment_afinn_ave, tokens_afinn_ave = afinn.Score(tweet,'Average')

print('Afinn score (Sum) =', sentiment_afinn_sum)
print('Afinn score (Average) =', sentiment_afinn_ave)
```
Afinn score (Sum) = 4.0  
Afinn score (Average) = 2.0
```python
print(tokens_afinn_sum)
print(tokens_afinn_sum == tokens_afinn_ave)
```
['best', 'easy']  
True

## POM

```python
GPOMS = sentiment_tools.GPOMS.GPOMS()

sentiment_gpoms_sum, tokens_gpoms_sum = GPOMS.Score(tweet,'Sum')
sentiment_gpoms_ave, tokens_gpoms_ave = GPOMS.Score(tweet,'Average')

for dimension in sentiment_gpoms_sum.keys():
	print(dimension + ' score (Sum) =', sentiment_gpoms_sum[dimension])
	print(dimension + ' score (Average) =', sentiment_gpoms_ave[dimension])
```
agreeable/hostile score (Sum) = 0.106  
agreeable/hostile score (Average) = 0.106  
confident/unsure score (Sum) = 0.737  
confident/unsure score (Average) = 0.737  
energetic/tired score (Sum) = 0.003  
energetic/tired score (Average) = 0.003  
composed/anxious score (Sum) = 0.023  
composed/anxious score (Average) = 0.023  
clearheaded/confused score (Sum) = 0.127  
clearheaded/confused score (Average) = 0.127  
elated/depressed score (Sum) = 0.0  
elated/depressed score (Average) = 0.0  
```python
print(tokens_gpoms_sum)
print(tokens_gpoms_sum == tokens_gpoms_ave)
```
{'agreeable/hostile': ['easy'], 'clearheaded/confused': ['easy'], 'composed/anxious': ['easy'], 'energetic/tired': ['easy'], 'confident/unsure': ['easy'], 'elated/depressed': []} 
True