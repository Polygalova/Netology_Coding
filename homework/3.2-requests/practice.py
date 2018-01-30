import requests
import chardet


def translate_it(text):
    lang_from = input('Исходный язык ')
    lang_to = input('Конечный язык ')
    if lang_to == '':
        lang_to = 'ru'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': key,
        'lang': lang_from + '-' + lang_to,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def get_text_write_result():
    path_from = input('Введите путь к файлу с текстом ')
    path_to = input('Введите путь к файлу с результатом ')
    with open(path_from, 'rb') as f:
        text_in = f.read()
        code_in = chardet.detect(text_in)
        text_in_decoded = text_in.decode(code_in['encoding'])
    text_out = translate_it(text_in_decoded)
    with open(path_to, 'w', encoding='utf8') as f:
        f.write(text_out)


get_text_write_result()
