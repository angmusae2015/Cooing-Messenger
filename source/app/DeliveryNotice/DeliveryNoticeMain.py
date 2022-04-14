from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime
from . import ScheduleSelectionWindow


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
                print(schedule)
