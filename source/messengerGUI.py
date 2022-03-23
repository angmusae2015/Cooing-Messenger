from PyQt5.QtWidgets import *
from PyQt5.QtCore import QMargins
import sys


def msgConfigLayout(parent):
    layout = QGridLayout()

    layout.addWidget(QLabel('발신 번호 선택'), 0, 0)

    selectNumBox = QComboBox()
    layout.addWidget(selectNumBox, 1, 0)
    layout.addWidget(QLabel('예약 시간 선택'), 0, 1)
    layout.addWidget(QCheckBox(), 0, 2)

    selectReserveTimeBox = QDateTimeEdit()
    layout.addWidget(selectReserveTimeBox, 1, 1, 1, 2)

    return layout


def fileSelectButtonLayout(parent):
    layout = QHBoxLayout()

    findButton = QPushButton("찾기", parent)
    findButton.setFixedWidth(50)
    layout.addWidget(findButton)

    fileNameViewer = QTextBrowser()
    fileNameViewer.setFixedHeight(findButton.height() - 5)
    layout.addWidget(fileNameViewer)

    return layout


def fileSelectLayout(parent):
    layout = QVBoxLayout()

    label = QLabel("일지 파일 선택(.xlsx)")
    layout.addWidget(label)
    layout.addLayout(fileSelectButtonLayout(parent))

    return layout


def sheetSelectLayout(parent):
    layout = QVBoxLayout()

    layout.addWidget(QLabel("불러올 시트 선택"))
    layout.addWidget(QComboBox())

    return layout


def sendButtonLayout(parent):
    layout = QHBoxLayout()

    layout.addStretch(1)

    sendButton = QPushButton('문자 보내기', parent)
    sendButton.setFixedWidth(150)
    sendButton.setFixedHeight(80)
    layout.addWidget(sendButton)

    return layout


def selectionAndSendLayout(parent):
    layout = QVBoxLayout()

    layout.addLayout(msgConfigLayout(parent))
    layout.addStretch(1)
    # layout.addSpacerItem(QSpacerItem(1, 5))
    layout.addLayout(fileSelectLayout(parent))
    layout.addStretch(1)
    # layout.addSpacerItem(QSpacerItem(1, 5))
    layout.addLayout(sheetSelectLayout(parent))
    layout.addStretch(1)
    # layout.addSpacerItem(QSpacerItem(1, 5))
    layout.addLayout(sendButtonLayout(parent))
    layout.addStretch(0)

    return layout


def msgPrevLayout(parent):
    layout = QVBoxLayout()

    layout.addWidget(QLabel('문자 미리보기'))

    msgSelection = QComboBox()
    layout.addWidget(msgSelection)

    msgPreview = QTextBrowser()
    msgPreview.setFixedHeight(200)
    layout.addWidget(msgPreview)

    return layout


def msgLayout(parent):
    layout = QHBoxLayout()
    layout.addLayout(selectionAndSendLayout(parent))
    layout.addLayout(msgPrevLayout(parent))

    return layout


def scheduleTableLayout(parent):
    layout = QVBoxLayout()

    layout.addLayout(msgLayout(parent))
    layout.addWidget(QTableWidget(10, 5), 10)

    return layout


app = QApplication([])
window = QWidget()
window.setLayout(scheduleTableLayout(window))
window.setGeometry(500, 500, 600, 600)
window.setFixedWidth(600)

window.show()
app.exec_()
