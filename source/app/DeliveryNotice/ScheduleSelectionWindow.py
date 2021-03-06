from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
import MemberTools
import ScheduleTools
import json


data_path = "../data/"
schedule_path = data_path + "Schedule.json"
book_list_path = data_path + "BookList.csv"
series_list_path = data_path + "SeriesList.csv"


class Layout(QGridLayout):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        self.selectedSchedules = []

        self.startDateLabel = QLabel('시작일')

        self.startDate = QDateEdit()
        self.startDate.setDate(QDate.currentDate())

        self.endDateLabel = QLabel('종료일')

        self.endDate = QDateEdit()
        self.endDate.setDate(QDate.currentDate())

        self.scheduleTable = ScheduleTable(self)

        self.findButton = FindButton(self)

        self.selectedStatus = SelectedStatus(self)

        self.addMsgButton = QPushButton('추가')

        self.addWidget(self.startDateLabel, 0, 0, 1, 2)
        self.addWidget(self.endDateLabel, 0, 5, 1, 2)
        self.addWidget(self.startDate, 1, 0, 1, 5)
        self.addWidget(self.endDate, 1, 5, 1, 5)
        self.addWidget(self.findButton, 2, 9)
        self.addWidget(self.scheduleTable, 4, 0, 5, 10)
        self.addWidget(self.selectedStatus, 10, 0)
        self.addWidget(self.addMsgButton, 10, 9)
        self.setRowStretch(4, 1)

        self.startDate.dateChanged.connect(self.change_end_date_range)
        self.endDate.dateChanged.connect(self.change_start_date_range)
        self.addMsgButton.clicked.connect(self.main_window.add_and_exit)

    def change_start_date_range(self):
        self.startDate.setMaximumDate(self.endDate.date())

    def change_end_date_range(self):
        self.endDate.setMinimumDate(self.startDate.date())

    def reset(self):
        self.findButton.reset_table()
        self.findButton.reset_selected_row()


class ScheduleTable(QTableWidget):
    def __init__(self, main_layout):
        super().__init__()

        self.main_layout = main_layout

        self.headers = ['', '운송장 번호', '배송일', '학생', '책', '무비랑']

        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.resizeColumnsToContents()


class FindButton(QPushButton):
    def __init__(self, main_layout: Layout):
        super().__init__()

        self.main_layout = main_layout
        self.setText('찾기')

        self.clicked.connect(self.reset_table)
        self.clicked.connect(self.fill_table)
        self.clicked.connect(self.reset_selected_row)

    def reset_table(self):
        self.main_layout.scheduleTable.setRowCount(0)

    def fill_table(self):
        start = self.main_layout.startDate.date().toPyDate()
        end = self.main_layout.endDate.date().toPyDate()
        sch_in_range = ScheduleTools.get_schedule_in_range(start, end)

        row_cnt = 0
        for row in sch_in_range:
            row_cnt += len(row['content'])

        self.main_layout.scheduleTable.setRowCount(row_cnt)

        crt_row = 0
        for row in sch_in_range:
            child_num = len(row['content'])
            family_id = row['family']

            if child_num > 1:
                for col in range(3):
                    self.main_layout.scheduleTable.setSpan(crt_row, col, child_num, 1)

            checkbox = TableCheckBox(self.main_layout, crt_row)
            self.main_layout.scheduleTable.setCellWidget(crt_row, 0, checkbox)

            item = tracking_num_table_item(ScheduleTools.get_tracking_num(row))
            self.main_layout.scheduleTable.setItem(crt_row, 1, item)    # add tracking number to table

            item = QTableWidgetItem(row['date'])
            self.main_layout.scheduleTable.setItem(crt_row, 2, item)    # add date to table

            for content in row['content']:
                item = child_name_table_item(family_id, content['child'])

                if item.text() == "Error":
                    checkbox.checkboxWidget.setDisabled(True)

                self.main_layout.scheduleTable.setItem(crt_row, 3, item)

                if content['book'] != 'SAME':
                    book_num = 0
                    for book in content['book']:
                        book_num += len(book['books'])

                    first_book = (content['book'][0]['series'], content['book'][0]['books'][0])
                    item = QTableWidgetItem(f"{first_book[0]}-{first_book[1]} 외 {book_num - 1}권")
                    self.main_layout.scheduleTable.setItem(crt_row, 4, item)

                crt_row += 1

        self.main_layout.scheduleTable.resizeColumnsToContents()
        self.main_layout.scheduleTable.resizeRowsToContents()

    def reset_selected_row(self):
        self.main_layout.selectedSchedules = []
        self.main_layout.selectedStatus.changeState(0)


class TableCheckBox(QWidget):
    def __init__(self, main_layout: Layout, row: int):
        super().__init__()

        self.main_layout = main_layout
        self.table = self.main_layout.scheduleTable

        self.layout = QHBoxLayout()

        self.checkboxWidget = QCheckBox()
        self.checkboxWidget.stateChanged.connect(self.select_row)
        self.layout.addWidget(self.checkboxWidget, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        self.row = row

    def select_row(self):
        self.table.clearSelection()

        for span in range(self.table.rowSpan(self.row, 0)):
            self.table.selectRow(self.row + span)

        selected_tracking_num = self.table.selectedItems()[0].text().replace('-', '')
        selected_schedule = ScheduleTools.get_schedule_by_num(selected_tracking_num)

        if self.checkboxWidget.checkState():
            self.main_layout.selectedSchedules.append(selected_schedule)

        else:
            self.main_layout.selectedSchedules.remove(selected_schedule)

        self.main_layout.selectedStatus.changeState(len(self.main_layout.selectedSchedules))


class SelectedStatus(QLabel):
    def __init__(self, main_layout):
        super().__init__()

        self.main_layout = main_layout
        self.value = 0

        self.changeState(0)

    def changeState(self, num):
        self.value = num
        self.setText(f"선택됨: {self.value}개")


def child_name_table_item(family_id: str, child_id: str):
    try:
        name = MemberTools.get_child_name(family_id, child_id)

    except MemberTools.MemberNotFoundError:
        name = "Error"

    return QTableWidgetItem(name)


def tracking_num_table_item(tracking_num: str):
    part1 = tracking_num[:4] + '-'
    part2 = tracking_num[4:8] + '-'
    part3 = tracking_num[8:]

    return QTableWidgetItem(part1 + part2 + part3)


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)

        self.lo = Layout(self)
        self.setLayout(self.lo)
        self.setGeometry(300, 300, 500, 500)

        self.add_button_pushed = False

    def add_and_exit(self):
        self.add_button_pushed = True
        self.close()
