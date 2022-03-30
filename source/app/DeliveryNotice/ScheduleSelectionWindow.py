from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
import pandas as pd
import re


data_path = "../data/"
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

        self.scheduleTable = QTableWidget()
        column_headers = ['배송일', '학생', '운송장 번호', '단계', '무비랑', '책']
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
        table = table[['Date', 'Child Num', 'Tracking Num', 'Step', 'Movierang', 'Books']]

        # table['Date'] =

        self.scheduleTable.setRowCount(table.shape[0])
        self.scheduleTable.setColumnCount(6)

        curRow = 0
        for row in table.index:
            for col in range(self.scheduleTable.columnCount()):
                value = table.loc[row][col]
                item = QTableWidgetItem(str(value))
                self.scheduleTable.setItem(curRow, col, item)

            curRow += 1

        self.scheduleTable.resizeColumnsToContents()

    # def addRow(self):


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)

        lo = Layout(self)
        self.setLayout(lo)
