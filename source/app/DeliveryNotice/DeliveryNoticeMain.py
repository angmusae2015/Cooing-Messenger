from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime
from . import ScheduleSelectionWindow
import MemberTools, BookTools
import json


with open("../data/Message.json") as f:
    base_msg = json.load(f)['delivery notice']


class Layout(QGridLayout):
    def __init__(self, main_window):
        super().__init__()

        self.scheduleSelectWindow = None
        self.main_window = main_window

        self.msg_list = []

        self.numSelectLabel = QLabel('발신 번호 선택')

        self.selectNumBox = QComboBox()

        self.dateTimeSelectLabel = QLabel('예약 시간 선택')

        self.toggleReserveMsg = QCheckBox()

        self.dateTimeSelectBox = QDateTimeEdit()
        self.dateTimeSelectBox.setEnabled(False)
        self.dateTimeSelectBox.setDateTime(QDateTime.currentDateTime())

        self.msgPrevLabel = QLabel('문자 미리보기')

        self.msgSelection = QComboBox()

        self.deleteMsg = QPushButton('삭제')

        self.msgPreview = QTextBrowser()

        self.selectScheduleButton = QPushButton('일정 선택')

        self.sendButton = QPushButton('문자 보내기')

        self.addWidget(self.numSelectLabel, 0, 0, 1, 2)
        self.addWidget(self.selectNumBox, 1, 0, 1, 2)
        self.addWidget(self.dateTimeSelectLabel, 0, 2, 1, 1)
        self.addWidget(self.toggleReserveMsg, 0, 3)
        self.addWidget(self.dateTimeSelectBox, 1, 2, 1, 2)
        self.addWidget(self.msgPrevLabel, 2, 0)
        self.addWidget(self.msgSelection, 3, 0, 1, 3)
        self.addWidget(self.deleteMsg, 3, 3)
        self.addWidget(self.msgPreview, 4, 0, 4, 4)
        self.setRowStretch(4, 1)
        self.addWidget(self.selectScheduleButton, 8, 0, 1, 2)
        self.addWidget(self.sendButton, 8, 2, 1, 2)

        self.toggleReserveMsg.stateChanged.connect(self.disableDateTimeEdit)
        self.selectScheduleButton.clicked.connect(self.showScheduleSelectionWindow)

    def disableDateTimeEdit(self):
        isChecked = self.toggleReserveMsg.isChecked()
        self.dateTimeSelectBox.setEnabled(isChecked)

    def showScheduleSelectionWindow(self):
        self.scheduleSelectWindow = ScheduleSelectionWindow.Window()
        self.scheduleSelectWindow.show()
        self.scheduleSelectWindow.exec_()

        if self.scheduleSelectWindow.add_button_pushed:
            for schedule in self.scheduleSelectWindow.lo.selectedSchedules:
                self.msg_list.append(self.write_msg(schedule))

    @staticmethod
    def write_msg(schedule):
        book_list_msg_dic = {}
        return_date = schedule['return request date']
        tracking_num = schedule['tracking num']

        for content in schedule['content']:
            child_name = MemberTools.get_child_name(content['child'])
            book_list_msg_dic[child_name] = []

            if content['book'] == 'SAME':
                book_list_msg_dic[child_name].append('상동\n\n')
                continue

            for book in content['book']:
                series_code = book['series']
                book_info_msg = ""
                book_info_msg += BookTools.get_series_name(series_code) + '\n'

                for vol in book['books']:
                    book_name = BookTools.get_book_name(series_code, vol)
                    book_info_msg += f"{vol}. {book_name}\n"

                book_info_msg += '\n'
                book_list_msg_dic[child_name].append(book_info_msg)

        book_list_msg = ""
        for name in book_list_msg_dic.keys():
            book_list_msg += name + '\n'

            for m in book_list_msg_dic[name]:
                book_list_msg += m

        msg = base_msg.format(book_list_msg, return_date, tracking_num)

        return msg
