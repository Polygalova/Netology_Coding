import osa
import math


def mid_temp_celsius(path):
    temp_in = []
    with open(path) as f:
        for line in f.readlines():
            temp_in.append(int(line.split()[0]))
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    temp_out = []
    for temp in temp_in:
        temp_out.append(client.service.ConvertTemp(temp, 'degreeFahrenheit', 'degreeCelsius'))
    print('Средняя температура за неделю: {} градусов Цельсия.'.format(sum(temp_out)/len(temp_out)))


def travel_amount(path):
    prices = []
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    with open(path) as f:
        for line in f.readlines():
            price, cur = line.split()[1:]
            prices.append(client.service.ConvertToNum('', cur, 'RUB', float(price), False))
    print('Стоимость путешествия: {} рублей.'.format(math.ceil(sum(prices))))


def amount_dist_km(path):
    distances = []
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    with open(path) as f:
        for line in f.readlines():
            distance = float(line.split()[1].replace(',', ''))
            distances.append(client.service.ChangeLengthUnit(distance, 'Miles', 'Kilometers'))
    print('Общая длина пути: {} км.'.format(round(sum(distances), 2)))


mid_temp_celsius('temps.txt')
travel_amount('currencies.txt')
amount_dist_km('travel.txt')



