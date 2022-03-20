"""
Program that make list of information of books and series
"""

from openpyxl import load_workbook
import csv


path = "data/original/책배송-진도.xlsx"    # original file
wb = load_workbook(path)

bookList = open("data/BookList.csv", 'a', newline='')    # csv file that saves book information
seriesList = open("data/SeriesList.csv", 'a', newline='')    # csv file that saves series information

wr1 = csv.writer(bookList)
wr2 = csv.writer(seriesList)

for ws in wb.worksheets:
    # title of work sheet should be "{num}.{series code}"
    seriesNum = ws.title.split('.')[0]  # number of series(str)
    seriesCode = ws.title.split('.')[1]     # series code(str)

    for row in ws.rows:
        if row[0].row == 1:     # if row 1 is selected, records series name in SeriesList.csv
            series = row[0].value
            wr2.writerow([seriesNum, seriesCode, series])
            continue

        if row[0].value is not None:    # if column A is not empty, records book information in BookList.csv
            wr1.writerow([seriesCode, row[0].value, row[1].value])

bookList.close()
seriesList.close()
