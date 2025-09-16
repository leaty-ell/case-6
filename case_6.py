# CASE-6
# DEVELOPERS: Ponasenko E., Limanova E., Loseva E.

import re
from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator


def sentn(text):
    sentences = re.split(r'[.!?]+', text)  # + означает один или более подряд
    sentences = [s for s in sentences if s.strip() != '']  # берем только непустые строки
    return sentences


def worrds(text):
    words = re.findall(r'\w+(?:-\w+)*', text)
    return words


def count_slogs(words):
    slogs = 0
    for word in words:
        for letter in word.lower():
            if letter in GLASNY:
                slogs += 1
    return slogs


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


def flesh_index(av_sentn_len, av_slogs_per_word):
    language = detect(text)
    if language == 'en':
        return 206.835 - 1.015 * av_sentn_len - 84.6 * av_slogs_per_word
    else:
        return 206.835 - 1.3 * av_sentn_len - 60.1 * av_slogs_per_word


def f_readability(flesh):
    if flesh > 80:
        return "Текст очень легко читается (для младших школьников)."
    elif flesh > 50:
        return "Простой текст (для школьников)."
    elif flesh > 25:
        return "Текст немного трудно читать (для студентов)."
    else:
        return "Текст трудно читается (для выпускников ВУЗов)."


def translate_text(text, target_language='en'):
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)


def analyze_sentiment(text):
    english_text = translate_text(text, 'en')

    analysis = TextBlob(english_text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0.1:
        sentiment = "позитивная"
    elif polarity < -0.1:
        sentiment = "негативная"
    else:
        sentiment = "нейтральная"

    return {
        "sentiment": sentiment,
        "subjectivity": subjectivity,
        "objectivity_percent": (1 - subjectivity) * 100,
        "subjectivity_percent": subjectivity * 100
    }


def main():
    av_sentn_len = len(worrds(text)) / len(sentn(text))
    av_slogs_per_word = count_slogs(worrds(text)) / len(worrds(text))

    language = def_lang(text)
    sentences = sentn(text)
    words_list = worrds(text)

    av_sentn_len = len(words_list) / len(sentences) if sentences else 0
    av_slogs_per_word = count_slogs(words_list) / len(words_list) if words_list else 0

    flesh = flesh_index(av_sentn_len, av_slogs_per_word)
    readability = f_readability(flesh)

    results=analyze_sentiment(text)

    print("Предложений:", len(sentn(text)))
    print("Слов:", len(worrds(text)))
    print("Слогов:", count_slogs(worrds(text)))
    print("Средняя длина предложения (в словах):", round(av_sentn_len, 3))
    print("Средняя длина слова (в слогах):", round(av_slogs_per_word, 2))
    print("Индекс удобчитаемости Флеша:", round(flesh, 2))
    print("Читаемость:", readability)
    print(f"Тональность: {results['sentiment']}")
    print(f"Объективность: {results['objectivity_percent']}%")





GLASNY = "ёeyuioaуеыаоэяи"
text = input(("Введите текст: "))

if __name__ == "__main__":
    main()

