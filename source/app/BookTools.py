import json

series_path = "../data/Series.json"
with open(series_path, encoding='utf-8') as f:
    series_dic = json.load(f)


def get_series_name(code: str):
    name = series_dic[code]['Name']

    return name


def get_book_name(series_code: str, vol: str):
    book_name = series_dic[series_code][vol]['Name']

    return book_name
