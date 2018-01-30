import requests
import chardet


def translate_it(path_from, path_to, lang_from, lang_to='ru'):
    with open(path_from, 'rb') as f:
        text_in = f.read()
        code_in = chardet.detect(text_in)
        text_in_decoded = text_in.decode(code_in['encoding'])
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': key,
        'lang': lang_from + '-' + lang_to,
        'text': text_in_decoded,
    }
    response = requests.get(url, params=params).json()
    text_out = ' '.join(response.get('text', []))

    with open(path_to, 'w', encoding='utf8') as f:
        f.write(text_out)


translate_it('DE.txt', 'DE_RU.txt', 'de')
translate_it('ES.txt', 'ES_RU.txt', 'es')
translate_it('FR.txt', 'FR_RU.txt', 'fr')
