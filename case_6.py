#CASE-6
#DEVELOPERS: Ponasenko E., Limanova E., Loseva E.

import re
from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator

def sentn(text):
    sentences = re.split(r'[.!?]+', text)   # + означает один или более подряд
    sentences = [s for s in sentences if s.strip() != ''] #берем только непустые строки
    return sentences

def worrds(text):
    words = re.findall(r'\w+(?:-\w+)*', text)
    return words

def count_slogs(words):
    slogs=0
    for word in words:
        for letter in word.lower():
            if letter in GLASNY:
                slogs += 1
    return slogs

def def_lang(text):
    language = detect(text)
    return language



GLASNY = "ёeyuioaуеыаоэяи"
text = input(("Введите текст: "))

def main():
    av_sentn_len = len(worrds(text)) / len(sentn(text))
    av_slogs_per_word = count_slogs(worrds(text)) / len(worrds(text))
    if def_lang(text) == 'en':
        flesh = 206.835 - 1.015 *  av_sentn_len - 84.6 * av_slogs_per_word
    else:
        flesh = 206.835 - 1.3 *  av_sentn_len - 60.1 * av_slogs_per_word

    if flesh > 80:
        readability = "Текст очень легко читается (для младших школьников)."
    elif flesh > 50:
        readability = "Простой текст (для школьников)."
    elif flesh > 25:
        readability = "Текст немного трудно читать (для студентов)."
    else:
        readability = "Текст трудно читается (для выпускников ВУЗов)."

    '''
    translator = GoogleTranslator(source="auto", target="en")
    translated = translator.translate(text)
    
    # Тональность
    blob = TextBlob(translated)
    if blob.sentiment.polarity > 0:
        tone = "позитивный"
    elif blob.sentiment.polarity < 0:
        tone = "негативный"
    else:
        tone = "нейтральный"

    # Объективность
    objectivity = (1 - blob.sentiment.subjectivity) * 100
    '''

    print("Предложений:", len(sentn(text)))
    print("Слов:", len(worrds(text)))
    print("Слогов:", count_slogs(worrds(text)))
    print("Средняя длина предложения (в словах):", round(av_sentn_len, 2))
    print("Средняя длина слова (в слогах):", round(av_slogs_per_word, 2))
    print("Индекс Флеша:", round(flesh, 2))
    print("Интерпретация:", readability)
    '''
    print("Тональность текста:", tone)
    print("Объективность:", round(objectivity, 1), "%")
    '''

if __name__ == "__main__":
    main()
