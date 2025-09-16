# CASE-6
# DEVELOPERS: Ponasenko E., Limanova E., Loseva E.

import re
from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator


def split_sentences(text):
    """
    Divides the text into sentences.
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip() != '']
    return sentences


def split_words(text):
    """
    Splits text into words.
    """
    words = re.findall(r'\w+(?:-\w+)*', text)
    return words


def count_syllables(words):
    """
    Counts the number of syllables in words.
    """
    syllables = 0
    for word in words:
        for letter in word.lower():
            if letter in VOWELS:
                syllables += 1
    return syllables


def detect_language(text):
    """
    Defines the language of the text.
    """
    language = detect(text)
    return language


def calculate_flesch_index(avg_sentence_length, avg_syllables_per_word, language):
    """
    Calculates the Flash Readability Index.
    """
    if language == 'en':
        return 206.835 - 1.015 * avg_sentence_length - 84.6 * avg_syllables_per_word
    else:
        return 206.835 - 1.3 * avg_sentence_length - 60.1 * avg_syllables_per_word


def get_readability_level(flesch_score):
    """
    Determines the level of readability according to the Flesch index.
    """
    if flesch_score > 80:
        return "Текст очень легко читается (для младших школьников)."
    elif flesch_score > 50:
        return "Простой текст (для школьников)."
    elif flesch_score > 25:
        return "Текст немного трудно читать (для студентов)."
    else:
        return "Текст трудно читается (для выпускников ВУЗов)."


def translate_text(text, target_language='en'):
    """
    Translates text into the specified language.
    """
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)


def analyze_sentiment(text):
    """
    Analyzes the tonality of the text.
    """
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
        "objectivity_percent": (1 - subjectivity) * 100
    }


def main():
    """
    The main function of text analysis.
    """
    sentences = split_sentences(text)
    words_list = split_words(text)
    language = detect_language(text)

    avg_sentence_length = len(words_list) / len(sentences)
    total_syllables = count_syllables(words_list)
    avg_syllables_per_word = total_syllables / len(words_list)

    flesch_score = calculate_flesch_index(
        avg_sentence_length,
        avg_syllables_per_word,
        language
    )
    readability = get_readability_level(flesch_score)
    sentiment_results = analyze_sentiment(text)

    print("Анализ текста:")
    print("Предложений:", len(sentences))
    print("Слов:", len(words_list))
    print("Слогов:", total_syllables)
    print("Средняя длина предложения (в словах):", round(avg_sentence_length, 3))
    print("Средняя длина слова (в слогах):", round(avg_syllables_per_word, 2))
    print("Индекс удобочитаемости Флеша:", round(flesch_score, 2))
    print("Читаемость:", readability)
    print(f"Тональность текста: {sentiment_results['sentiment']}")
    print(f"Объективность: {round(sentiment_results['objectivity_percent'], 1)}%")


VOWELS = "ёeyuioaуеыаоэяи"
text = input("Введите текст: ")

if __name__ == "__main__":
    main()

