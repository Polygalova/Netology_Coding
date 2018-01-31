import requests
'''
auth_url = 'https://oauth.vk.com/authorize'
app_id = 6352609
auth_data = {
    'client_id': app_id,
    'scope': 'friends',
    'response_type': 'token'
}
from urllib.parse import urlencode
print('?'.join((auth_url, urlencode(auth_data))))
https://oauth.vk.com/blank.html#access_token=a33983f3868e87d73176bf8b96e7ac0b08a206ee7ea4721660ac56c1582c2407813200a6c6e073ecb7dbe&expires_in=86400&user_id=7318639
token = 'a33983f3868e87d73176bf8b96e7ac0b08a206ee7ea4721660ac56c1582c2407813200a6c6e073ecb7dbe'
'''


def get_mutual_friends(token, source_uid, target_uid):
    params = {
        'access_token': token,
        'source_uid': source_uid,
        'target_uid': target_uid
    }
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    result = response.json()['response']
    return set(result)


def print_total_mutual():
    token = 'a33983f3868e87d73176bf8b96e7ac0b08a206ee7ea4721660ac56c1582c2407813200a6c6e073ecb7dbe'
    ids = [int(num) for num in input('Введите идентификаторы пользователей через запятую ').split(', ')]
    n = len(ids)
    pairs_mutual = []

    for i in range(0, n, 2):
        try:
            pairs_mutual.append(get_mutual_friends(token, ids[i], ids[i+1]))
        except:
            pairs_mutual.append(get_mutual_friends(token, ids[i], ids[0]))
    result_set = pairs_mutual[0]
    for friend in pairs_mutual:
        result_set &= friend
    print('Общие друзья:')
    for user in result_set:
        print('id пользователя: {0}, ссылка на страничку: {1}'.format(user, 'https://vk.com/id' + str(user)))


print_total_mutual()
