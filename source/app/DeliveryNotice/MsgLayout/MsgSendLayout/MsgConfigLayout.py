from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime


class layout(QGridLayout):
    def __init__(self):
        super().__init__()

        self.numSelectLabel = QLabel('발신 번호 선택')

        self.selectNumBox = QComboBox()

        self.dateTimeSelectLabel = QLabel('예약 시간 선택')

        self.toggleReserveMsg = QCheckBox()

        self.dateTimeSelectBox = QDateTimeEdit()
        self.dateTimeSelectBox.setEnabled(False)
        self.dateTimeSelectBox.setDateTime(QDateTime.currentDateTime())

        self.addWidget(self.numSelectLabel, 0, 0, 1, 2)
        self.addWidget(self.selectNumBox, 1, 0, 1, 2)
        self.addWidget(self.dateTimeSelectLabel, 0, 2, 1, 1)
        self.addWidget(self.toggleReserveMsg, 0, 3)
        self.addWidget(self.dateTimeSelectBox, 1, 2, 1, 2)

        self.toggleReserveMsg.stateChanged.connect(self.disableDateTimeEdit)

    def disableDateTimeEdit(self):
        isChecked = self.toggleReserveMsg.isChecked()
        self.dateTimeSelectBox.setEnabled(isChecked)
