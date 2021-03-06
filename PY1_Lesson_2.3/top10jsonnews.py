# coding: utf-8
import json
import chardet


def open_and_decoding(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        news = json.loads(s)
        return news


def separate_words(file_name):
    news_dict = open_and_decoding(file_name)
    s = ''
    for row in news_dict['rss']['channel']['items']:
        s += ' ' + row['description']
    return s.strip().split()


def get_dict_word_quantity(news):
    words_quantity = {}
    for word in news:
        if len(word) > 6:
            quantity = news.count(word)
            words_quantity[word] = quantity
    return words_quantity


def get_arr_of_quantity(words_quantity):
    arr_of_quantity = []
    for value in words_quantity.values():
        arr_of_quantity.append(value)
    arr_of_quantity.sort(reverse=True)
    return arr_of_quantity


def print_top10(file_name):
    news = separate_words(file_name)
    words_quantity_dict = get_dict_word_quantity(news)
    arr_of_quantity = get_arr_of_quantity(words_quantity_dict)

    counter = 0
    print('Top 10 words for file {}:'.format(file_name))
    for i in range(10):
        for key, value in words_quantity_dict.items():
            if value == arr_of_quantity[i]:
                print('{}: {} times'.format(key, value))
                counter += 1
                if counter == 10:
                    print()
                    return


print_top10('newsfr.json')
print_top10('newsit.json')
print_top10('newsafr.json')
print_top10('newscy.json')
