from textblob import TextBlob
def analysis_sentiment(text):
    blob= TextBlob(text)

    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        sentiment_category = "Positive"
    elif polarity < 0:
        sentiment_category = "Negative"
    else:
        sentiment_category = "Neutral"
    
    return sentiment_category

text = input("Enter your text:")
result = analysis_sentiment(text)

print(f"Sentiment: {result}")

    