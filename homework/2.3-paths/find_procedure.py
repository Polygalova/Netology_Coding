import os


def get_sql(dir_for_search):
    found_files = set()
    for root, dirs, files in os.walk(dir_for_search):
        for filename in files:
            if filename[-4:] == '.sql':
                found_files.add(filename)
    return found_files, len(found_files)


def search_by_string(files, dir_for_search):
    found_files = set()
    string_for_search = input('Введите строку: ').lower()
    for filename in files:
        with open(os.path.join(dir_for_search, filename), 'r') as f:
            if string_for_search in f.read().lower():
                found_files.add(filename)
    for name in found_files:
        print(os.path.join(dir_for_search, name))
    count = len(found_files)
    print('Всего:', count)
    return found_files, count


def find_sql_by_string():
    migrations = 'Migrations/'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dir_for_search = os.path.dirname(os.path.join(current_dir, migrations))
    if __name__ == '__main__':
        found_files, count = get_sql(dir_for_search)
        while count > 1:
            found_files, count = search_by_string(found_files, dir_for_search)


find_sql_by_string()
