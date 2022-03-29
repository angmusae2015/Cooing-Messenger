from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
import pandas as pd
import re


data_path = "../../data/"
schedule_path = data_path + "Schedule.csv"
book_list_path = data_path + "BookList.csv"
series_list_path = data_path + "SeriesList.csv"


class Layout(QGridLayout):
    def __init__(self, mainWindow):
        super().__init__()

        self.mainWindow = mainWindow

        self.sch = pd.read_csv(schedule_path, parse_dates=['Date', 'Return Request Date'], dtype=str)

        self.selectedSchedules = []

        self.startDateLabel = QLabel('시작일')

        self.startDate = QDateEdit()
        self.startDate.setDate(QDate.currentDate())

        self.endDateLabel = QLabel('종료일')

        self.endDate = QDateEdit()
        self.endDate.setDate(QDate.currentDate())

        self.searchButton = QPushButton('찾기')

        self.scheduleTable = QTableWidget(10, 10)

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

    def changeStartDateRange(self):
        self.startDate.setMaximumDate(self.endDate.date())

    def changeEndDateRange(self):
        self.endDate.setMinimumDate(self.startDate.date())

    def searchByDate(self):
        start = pd.to_datetime(self.startDate.date().toPyDate())
        end = pd.to_datetime(self.endDate.date().toPyDate())
        table = self.sch[(self.sch['Date'] >= start) and (self.sch['Date'] <= end)]


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)

        lo = Layout(self)
        self.setLayout(lo)
