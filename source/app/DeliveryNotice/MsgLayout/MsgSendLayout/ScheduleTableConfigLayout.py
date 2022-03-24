from PyQt5.QtWidgets import *


class layout(QGridLayout):
    def __init__(self, parent):
        super().__init__()

        self.fileSelectLabel = QLabel('일지 파일 선택(.xlsx)')

        self.findButton = QPushButton("찾기", parent)
        self.findButton.setFixedWidth(50)

        self.fileNameViewer = QTextBrowser()
        self.fileNameViewer.setFixedHeight(self.findButton.height() - 5)

        self.sheetSelectLabel = QLabel('불러올 시트 선택')

        self.sheetSelectBox = QComboBox()

        self.addWidget(self.fileSelectLabel, 0, 0, 1, 2)
        self.addWidget(self.findButton, 1, 0)
        self.addWidget(self.fileNameViewer, 1, 1, 1, 2)
        self.addWidget(self.sheetSelectLabel, 2, 0, 1, 2)
        self.addWidget(self.sheetSelectBox, 3, 0, 1, 3)
