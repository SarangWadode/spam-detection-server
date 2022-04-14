from django.db.models import QuerySet
from textblob import TextBlob

def create_json(results: QuerySet, start: int):
    return {
        'count': results.count(),
        'results': list(results),
        'start': start
    }

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.polarity
    sentiment = 'neutral' if polarity == 0 else 'negative' if polarity < 0 else 'positive'

    return sentiment, round(abs(polarity), 7)
