import pandas as pd
import json

series_path = "../data/Series.json"
with open(series_path, encoding='utf-8') as f:
    series_dic = json.load(f)


book_path = "../data/BookList.csv"
book_df = pd.read_csv(book_path, dtype=str)


def get_series_name(code: str):
    name = series_dic[code]['Name']

    return name


def get_book_name(series_code: str, num: str):
    series_df = book_df[book_df['Series'] == series_code]
    book_name = series_df[series_df['Num'] == num]['Name'].values[0]

    return book_name
