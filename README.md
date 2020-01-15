# How to use

Some techniques have two possible methods. `Sum` finds the sum of the values per tweet while `Average` finds the mean value per tweet. Only words with a score are counted. the `Score()` function return a score and a list of tokens. This is returned for each dimension of a sentiment type, if possible.

```python
tweet = 'This tool is easy and fun to use!!!'
```

## Opinion Finder

```python
from moodscores import opinionfinder
OF = opinionfinder.OpinionFinder()

sentiment_sum,tokenized_list_of_words_sum = OF.Score(tweet,'Sum')
sentiment_ave,tokenized_list_of_words_ave = OF.Score(tweet,'Average')

print('OpinionFinder Sum =', sentiment_sum)
print('OpinionFinder Average =', sentiment_ave)
print('Tokenized list (from Sum) =', tokenized_list_of_words_sum)
print('Tokens are the same =' ,tokenized_list_of_words_ave == tokenized_list_of_words_sum)
```
OpinionFinder Sum = 2.0
OpinionFinder Average = 1.0

Tokenized list (from Sum) = ['easy', 'fun']

Tokens are the same = True

## Vader

```python
from moodscores import custom_vader
vader = custom_vader.SentimentIntensityAnalyzer()

sentiment_vader, tokenized_list_of_words_vader = vader.polarity_scores(tweet)

print('Vader Scoring Dimensions =', list(sentiment_vader.keys()))
for dimension in sentiment_vader.keys():
	 	print(dimension + ' score =', sentiment_vader[dimension])
print('Tokenized list =', tokenized_list_of_words_vader)
```
Vader Scoring Dimensions = ['neg', 'neu', 'pos', 'compound']

neg score = 0.0
neu score = 0.459
pos score = 0.541
compound score = 0.795

Tokenized list = ['easy', 'fun']

## ANEW

```python
from moodscores import anew
ANEW = anew.Anew()

sentiment_sum,tokenized_list_of_words_sum = ANEW.Score(tweet,'Sum')
sentiment_ave,tokenized_list_of_words_ave = ANEW.Score(tweet,'Average')

print('ANEW Scoring Dimensions =', list(sentiment_sum.keys()))
for dimension in sentiment_sum.keys():
	print(dimension + ' score (Sum) =', sentiment_sum[dimension])
	print(dimension + ' score (Average) =', sentiment_ave[dimension])
print('Tokenized List =', tokenized_list_of_words_sum)
print('Tokens are the same =', tokenized_list_of_words_sum == tokenized_list_of_words_ave)
```
ANEW Scoring Dimensions = ['Valence', 'Arousal', 'Dominance']

Valence score (Sum) = 26.089999999999996
Valence score (Average) = 6.522499999999999
Arousal score (Sum) = 18.240000000000002
Arousal score (Average) = 4.5600000000000005
Dominance score (Sum) = 24.81
Dominance score (Average) = 6.2025

Tokenized List = ['tool', 'easy', 'fun', 'use']

Tokens are the same = True

## Custom Vader - can be used with any dictionary in the package such as ANEW, but can also take custom inputs

By default, this uses the lexicon and emoji_lexicon from Vader. But, the lexicon can be replaced by other values. The parameter `lexicon` can take the location to an input file or the following values:

* Vader - VADER
* OF - OpinionFinder
* ANEW_Valence - Valence dimension of ANEW
* ANEW_Dominance - Dominance dimension of ANEW
* ANEW_Arousal - Arousal dimension of ANEW
* GPOMS_composed/anxious - composed/anxious dimension of GPOMS
* GPOMS_agreeable/hostile - agreeable/hostile dimension of GPOMS
* GPOMS_elated/depressed - elated/depressed dimension of GPOMS
* GPOMS_confident/unsure - confident/unsure dimension of GPOMS
* GPOMS_clearheaded/confused - clearheaded/confused dimension of GPOMS
* GPOMS_energetic/tired - energetic/tired dimension of GPOMS

```python
from moodscores import custom_vader
arousal_vader = custom_vader.SentimentIntensityAnalyzer(lexicon = 'ANEW_Arousal')
valence_vader = custom_vader.SentimentIntensityAnalyzer(lexicon = 'ANEW_Valence')
dominance_vader = custom_vader.SentimentIntensityAnalyzer(lexicon = 'ANEW_Dominance')

a_sentiment, a_tokens = arousal_vader.polarity_scores(tweet)
v_sentiment, v_tokens = valence_vader.polarity_scores(tweet)
d_sentiment, d_tokens = dominance_vader.polarity_scores(tweet)

for dimension in a_sentiment.keys():
	print('Arousal score ' + dimension + ' =', a_sentiment[dimension])
	print('Valence score ' + dimension + ' =', v_sentiment[dimension])
	print('Dominance score ' + dimension + ' =', d_sentiment[dimension])

print('Tokenized list =', a_tokens)
print('Tokens are the same =', a_tokens == v_tokens == d_tokens)
```
Arousal score neg = 0.0
Valence score neg = 0.0
Dominance score neg = 0.0
Arousal score neu = 0.148
Valence score neu = 0.114
Dominance score neu = 0.119
Arousal score pos = 0.852
Valence score pos = 0.886
Dominance score pos = 0.881
Arousal score compound = 0.9801
Valence score compound = 0.9898
Dominance score compound = 0.9888

Tokenized list = ['tool', 'easy', 'fun', 'use']

Tokens are the same = True

## Afinn

```python
from moodscores import afinn
afinn = afinn.Afinn()

sentiment_afinn_sum, tokens_afinn_sum = afinn.Score(tweet,'Sum')
sentiment_afinn_ave, tokens_afinn_ave = afinn.Score(tweet,'Average')

print('Afinn score (Sum) =', sentiment_afinn_sum)
print('Afinn score (Average) =', sentiment_afinn_ave)
print('Tokenized list =', tokens_afinn_sum)
print('Tokens are the same =', tokens_afinn_sum == tokens_afinn_ave)
```
Afinn score (Sum) = 5.0
Afinn score (Average) = 2.5

Tokenized list = ['easy', 'fun']
Tokens are the same = True

## GPOM

```python
from moodscores import gpoms
GPOMS = gpoms.GPOMS()

sentiment_gpoms_sum, tokens_gpoms_sum = GPOMS.Score(tweet,'Sum')
sentiment_gpoms_ave, tokens_gpoms_ave = GPOMS.Score(tweet,'Average')

for dimension in sentiment_gpoms_sum.keys():
	print(dimension + ' score (Sum) =', sentiment_gpoms_sum[dimension])
	print(dimension + ' score (Average) =', sentiment_gpoms_ave[dimension])

print('Tokenized list =', tokens_gpoms_sum)
```

composed/anxious score (Sum) = 0.15999999999999998
composed/anxious score (Average) = 0.07999999999999999
agreeable/hostile score (Sum) = 0.436
agreeable/hostile score (Average) = 0.218
elated/depressed score (Sum) = 0.237
elated/depressed score (Average) = 0.237
confident/unsure score (Sum) = 0.763
confident/unsure score (Average) = 0.3815
clearheaded/confused score (Sum) = 0.14300000000000002
clearheaded/confused score (Average) = 0.07150000000000001
energetic/tired score (Sum) = 0.251
energetic/tired score (Average) = 0.1255

Tokenized list = {'composed/anxious': ['easy', 'fun'], 'agreeable/hostile': ['easy', 'fun'], 'elated/depressed': ['fun'], 'confident/unsure': ['easy', 'fun'], 'clearheaded/confused': ['easy', 'fun'], 'energetic/tired': ['easy', 'fun']}