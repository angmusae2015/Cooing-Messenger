from PyQt5.QtWidgets import *
import sys


def msgConfigLayout(parent):
    layout = QGridLayout()

    layout.addWidget(QLabel('발신 번호 선택'), 0, 0)

    selectNumBox = QComboBox()
    selectNumBox.setPlaceholderText("발신 번호 선택")
    layout.addWidget(selectNumBox, 1, 0)
    layout.addWidget(QLabel('예약 시간 선택'), 0, 1)

    selectReserveTimeBox = QDateTimeEdit()
    layout.addWidget(selectReserveTimeBox, 1, 1)

    return layout


def fileSelectLayout(parent):
    layout = QGridLayout()
    label = QLabel("일지 파일 선택(.xlsx)")
    layout.addWidget(label, 0, 0, 0, 1)

    space = QSpacerItem(100, 30)
    layout.addItem(space, 1, 0, 1, 1)

    findButton = QPushButton("찾기", parent)
    layout.addWidget(findButton, 2, 0)

    fileNameViewer = QTextBrowser()
    fileNameViewer.setFixedHeight(findButton.height())
    layout.addWidget(fileNameViewer, 2, 1)

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

    msgPreview = QTextBrowser()
    layout.addWidget(msgPreview)

    return layout


def scheduleTableLayout(parent):
    layout = QVBoxLayout()
    layout.addLayout(msgPrevLayout(parent))
    layout.addWidget(QTableWidget(10, 10))

    return layout


app = QApplication([])
window = QWidget()
window.setLayout(scheduleTableLayout(window))
window.show()
app.exec_()
