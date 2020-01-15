from nltk.tokenize import TweetTokenizer

def tokenizer(tweet, case = 'lower'):
    tknzr = TweetTokenizer()
    if case == 'lower': 
    	return tknzr.tokenize(tweet.lower())
    else: 
    	tknzr.tokenize(tweet)
    