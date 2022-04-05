from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
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

        self.sch = pd.read_csv(schedule_path, parse_dates=['Date'], dtype=str)
        self.sch = self.sch[self.sch.columns[:5]]
        self.sch.fillna('', inplace=True)

        self.showedSchedules = []
        self.selectedSchedules = []

        self.startDateLabel = QLabel('시작일')

        self.startDate = QDateEdit()
        self.startDate.setDate(QDate.currentDate())

        self.endDateLabel = QLabel('종료일')

        self.endDate = QDateEdit()
        self.endDate.setDate(QDate.currentDate())

        self.scheduleTable = ScheduleTable()

        self.searchButton = FindButton(self.scheduleTable)

        self.selectedStatus = QLabel('선택됨: ')

        self.addMsgButton = QPushButton('추가')

        self.addWidget(self.startDateLabel, 0, 0, 1, 2)
        self.addWidget(self.endDateLabel, 0, 5, 1, 2)
        self.addWidget(self.startDate, 1, 0, 1, 5)
        self.addWidget(self.endDate, 1, 5, 1, 5)
        self.addWidget(self.searchButton, 2, 9)
        self.addWidget(self.scheduleTable, 4, 0, 5, 10)
        self.addWidget(self.selectedStatus, 10, 0)
        self.addWidget(self.addMsgButton, 10, 9)
        self.setRowStretch(4, 1)

        self.startDate.dateChanged.connect(self.change_end_date_range)
        self.endDate.dateChanged.connect(self.change_start_date_range)
        self.searchButton.clicked.connect(self.fill_table)

    def change_start_date_range(self):
        self.startDate.setMaximumDate(self.endDate.date())

    def change_end_date_range(self):
        self.endDate.setMinimumDate(self.startDate.date())

    def fill_table(self):
        start = pd.to_datetime(self.startDate.date().toPyDate())
        end = pd.to_datetime(self.endDate.date().toPyDate())
        scheduleDf = self.sch[(self.sch['Date'] >= start) & (self.sch['Date'] <= end)]
        scheduleDf['Date'] = [date.date() for date in scheduleDf['Date']]

        self.scheduleTable.setRowCount(scheduleDf.shape[0])

        funcList = [
            date_table_item,
            child_name_table_item,
            tracking_num_table_item,
            QTableWidgetItem,
            QTableWidgetItem
        ]

        for row in scheduleDf.index:
            rowIndex = row - scheduleDf.index[0]
            checkBox = TableCheckBox(self, rowIndex)
            self.scheduleTable.setCellWidget(rowIndex, 0, checkBox)

            for column in scheduleDf.columns:
                columnIndex = list(scheduleDf.columns).index(column)
                value = scheduleDf.loc[row, column]

                self.scheduleTable.setItem(row - scheduleDf.index[0], columnIndex + 1, funcList[columnIndex](value))

        self.scheduleTable.resizeColumnsToContents()
        self.scheduleTable.resizeRowsToContents()


class ScheduleTable(QTableWidget):
    def __init__(self):
        super().__init__()

        self.headers = ['', '배송일', '학생', '운송장 번호', '책', '무비랑']
        self.selectedRows = []

        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resizeColumnsToContents()


class FindButton(QPushButton):
    def __init__(self, table):
        super().__init__()

        self.table = table
        self.setText('찾기')


class TableCheckBox(QWidget):
    def __init__(self, mainLayout: Layout, row: int):
        super().__init__()

        self.mainLayout = mainLayout
        self.table = self.mainLayout.scheduleTable

        self.layout = QHBoxLayout()

        self.checkboxWidget = QCheckBox()
        self.checkboxWidget.stateChanged.connect(self.select_row)
        self.layout.addWidget(self.checkboxWidget, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        self.row = row

    def select_row(self):
        self.table.clearSelection()
        self.table.selectRow(self.row)

        if self.checkboxWidget.checkState():
            self.table.selectedRows.append(self.table.selectedItems())

        else:
            self.table.selectedRows.remove(self.table.selectedItems())


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


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)

        lo = Layout(self)
        self.setLayout(lo)
        self.setGeometry(300, 300, 500, 500)
