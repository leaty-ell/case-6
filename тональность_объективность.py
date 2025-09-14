def def_lang(text):
    language = detect(text)
    return language

def analyze_sentiment(text, language):
    if language == 'en':
        blob = TextBlob(text)
    else:
        blob = TextBlob(text)
        blob = blob.translate(to='en')

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

if polarity > 0:
        tone = "позитивный"
    elif polarity < 0:
        tone = "негативный"
    else:
        tone = "нейтральный"

    return tone, subjectivity
