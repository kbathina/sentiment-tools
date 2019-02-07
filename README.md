import sentiment_tools


vader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer()
vader.polarity_scores('good')


cvader = sentiment_tools.custom_vader.SentimentIntensityAnalyzer(lex_dict='sentiment_tools/OpFi-Sent.txt', lex_sep= ' ')
cvader.polarity_scores('good')


norm = sentiment_tools.Norm.Norm()
print(norm.Score('good and bad','Sum'))
print(norm.Score('good and bad','Average'))


OF = sentiment_tools.OpinionFinder.OpinionFinder()
print(OF.Score('good and good','Sum'))
print(OF.Score('good and good','Average'))


POM = sentiment_tools.Pom.Pom()
print(POM.Score('good and good','Sum'))
print(POM.Score('good and good','Average'))