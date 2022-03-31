from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
import pandas as pd
import MemberTools
import datetime


data_path = "../data/"
schedule_path = data_path + "Schedule.csv"
book_list_path = data_path + "BookList.csv"
series_list_path = data_path + "SeriesList.csv"
member_path = data_path + "Member.csv"


memberTable = pd.read_csv(member_path, dtype=str)


class Layout(QGridLayout):
    def __init__(self, mainWindow):
        super().__init__()

        self.mainWindow = mainWindow

        self.sch = pd.read_csv(schedule_path, parse_dates=['Date', 'Return Request Date'], dtype=str)
        self.sch = self.sch[self.sch.columns[:4]]

        self.selectedSchedules = []

        self.startDateLabel = QLabel('시작일')

        self.startDate = QDateEdit()
        self.startDate.setDate(QDate.currentDate())

        self.endDateLabel = QLabel('종료일')

        self.endDate = QDateEdit()
        self.endDate.setDate(QDate.currentDate())

        self.searchButton = QPushButton('찾기')

        self.scheduleTable = QTableWidget()
        column_headers = ['배송일', '학생', '운송장 번호', '책']
        self.scheduleTable.setColumnCount(len(column_headers))
        self.scheduleTable.setHorizontalHeaderLabels(column_headers)
        self.scheduleTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.scheduleTable.resizeColumnsToContents()

        self.addMsgButton = QPushButton('추가')

        self.addWidget(self.startDateLabel, 0, 0, 1, 2)
        self.addWidget(self.endDateLabel, 0, 5, 1, 2)
        self.addWidget(self.startDate, 1, 0, 1, 5)
        self.addWidget(self.endDate, 1, 5, 1, 4)
        self.addWidget(self.searchButton, 2, 8)
        self.addWidget(self.scheduleTable, 4, 0, 5, 9)
        self.addWidget(self.addMsgButton, 10, 8)
        self.setRowStretch(4, 1)

        self.startDate.dateChanged.connect(self.changeEndDateRange)
        self.endDate.dateChanged.connect(self.changeStartDateRange)
        self.searchButton.clicked.connect(self.fillTable)

    def changeStartDateRange(self):
        self.startDate.setMaximumDate(self.endDate.date())

    def changeEndDateRange(self):
        self.endDate.setMinimumDate(self.startDate.date())

    def fillTable(self):
        start = pd.to_datetime(self.startDate.date().toPyDate())
        end = pd.to_datetime(self.endDate.date().toPyDate())
        table = self.sch[(self.sch['Date'] >= start) & (self.sch['Date'] <= end)]
        table['Date'] = [date.date() for date in table['Date']]

        self.scheduleTable.setRowCount(table.shape[0])
        self.scheduleTable.setColumnCount(6)

        funcList = [date_table_item, child_name_table_item, tracking_num_table_item, book_table_item]
        for row in table.index:
            for column in table.columns:
                columnIndex = list(table.columns).index(column)
                value = table.loc[row][column]

                self.scheduleTable.setItem(row - table.index[0], columnIndex, funcList[columnIndex](value))

        self.scheduleTable.resizeColumnsToContents()


def to_table_item(func):
    def wrapper(data):
        value = func(data)
        return QTableWidgetItem(value)

    return wrapper


@to_table_item
def date_table_item(date: datetime.date):
    return "{0.year}-{0.month}-{0.day}".format(date)


@to_table_item
def child_name_table_item(childNum: str):
    return MemberTools.get_child_name(memberTable, childNum)


@to_table_item
def tracking_num_table_item(trackingNum: str):
    part1 = trackingNum[:4] + '-'
    part2 = trackingNum[4:8] + '-'
    part3 = trackingNum[8:]

    return part1 + part2 + part3


@to_table_item
def book_table_item(book: str):
    return book


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)

        lo = Layout(self)
        self.setLayout(lo)
