from PyQt5.QtWidgets import *
import sys


def msgConfigLayout(parent):
    layout = QGridLayout()

    layout.addWidget(QLabel('발신번호 선택'), 0, 0)

    selectNumBox = QComboBox()
    selectNumBox.setPlaceholderText("발신번호 선택")
    layout.addWidget(selectNumBox, 1, 0)
    layout.addWidget(QLabel('예약 시간 선택'), 0, 1)

    selectReserveTimeBox = QDateTimeEdit()
    layout.addWidget(selectReserveTimeBox, 1, 1)

    return layout


def fileSelectLayout(parent):
    layout = QGridLayout()
    label = QLabel("일지 파일 선택(.xlsx)")
    layout.addWidget(label, 0, 0, 0, 2)

    findButton = QPushButton("찾기", parent)
    layout.addWidget(findButton, 1, 0)

    fileNameViewer = QTextBrowser()
    fileNameViewer.setFixedHeight(findButton.height())
    layout.addWidget(fileNameViewer, 1, 1)

    return layout


def sheetSelectLayout(parent):
    layout = QVBoxLayout()
    layout.addWidget(QLabel("불러올 시트 선택"))
    layout.addWidget(QComboBox())

    return layout


def selectionLayout(parent):
    layout = QVBoxLayout()
    layout.addLayout(msgConfigLayout(parent))
    layout.addLayout(fileSelectLayout(parent))
    layout.addLayout(sheetSelectLayout(parent))

    return layout


def msgPrevLayout(parent):
    layout = QHBoxLayout()
    layout.addLayout(selectionLayout(parent))
    layout.addWidget(QTextBrowser())

    return layout


def scheduleTableLayout(parent):
    layout = QVBoxLayout()
    layout.addLayout(msgPrevLayout(parent))
    layout.addWidget(QTableWidget(10, 10))

    return layout


app = QApplication([])


"""
selectNumLabel = QLabel()
selectNumLabel.setText("발신번호 선택")

selectReserveTimeLabel = QLabel()
selectReserveTimeLabel.setText("예약 시간 선택")

selectNum = QComboBox()
selectNum.setPlaceholderText("발신번호 선택")

selectReserveTime = QDateTimeEdit()

msgConfig = QGridLayout()
msgConfig.addWidget(selectNumLabel, 0, 0)
msgConfig.addWidget(selectNum, 1, 0)
msgConfig.addWidget(selectReserveTimeLabel, 0, 1)
msgConfig.addWidget(selectReserveTime, 1, 1)
"""

window = QWidget()
window.setLayout(scheduleTableLayout(window))
window.show()
app.exec_()
