# How to use

## Some techniques have two possible methods. 'Sum' finds the sum of the values per tweet while 'Average' finds the mean value per tweet. Only words with a score are counted.

## Returns NA if there are no words that match. 

```python
import sentiment_tools
tweet = 'This package is great!!'
```

## Opinion Finder

```python
OF = sentiment_tools.OpinionFinder.OpinionFinder()

OF.Score(tweet,'Sum')
OF.Score(tweet,'Average')
```

## Vader

```python
vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer()

vader.polarity_scores(tweet)
```


## Vader with Opinion Finder

```python
OF_Vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/OpFi-Sent.txt', lex_sep= ' ')

OF_Vader.polarity_scores(tweet)
```

## Anew

```python
norm = sentiment_tools.Norm.Norm()

norm.Score(tweet,'Sum')
norm.Score(tweet,'Average')

def Anew_Splitter(tweet, method):
    r = anew.Score(tweet, method)
    return [r['Valence'],r['Dominance'],r['Arousal']]

Anew_Splitter(tweet, 'Sum')
```

## Vader with Anew

```python
arousal_vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/Anew_arousal.txt', lex_sep= '\t')
valence_vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/Anew_valence.txt', lex_sep= '\t')
dominance_vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/Anew_dominance.txt', lex_sep= '\t')


arousal_vader.polarity_scores(tweet)
valence_vader.polarity_scores(tweet)
dominance_vader.polarity_scores(tweet)
```


## Afinn

```python
afinn = sentiment_tools.Afinn.Afinn()

afinn.Score(tweet,'Sum')
afinn.Score(tweet,'Average')
```


## POM

```python
POM = sentiment_tools.Pom.Pom()

POM.Score(tweet,'Sum')
POM.Score(tweet,'Average')

## Function to split up results to list
def Pom_Splitter(tweet, method):
    r = POM.Score(tweet, method)
    return [r['composed/anxious'],r['agreeable/hostile'],r['elated/depressed'],r['confident/unsure'],r['clearheaded/confused'],r['energetic/tired']]

Pom_Splitter(tweet, 'Sum')
```