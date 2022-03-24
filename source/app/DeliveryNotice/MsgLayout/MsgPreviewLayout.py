from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QTextBrowser


class layout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.label = QLabel('문자 미리보기')

        self.msgSelection = QComboBox()

        self.msgPreview = QTextBrowser()
        self.msgPreview.setFixedHeight(200)

        self.addWidget(self.label)
        self.addWidget(self.msgSelection)
        self.addWidget(self.msgPreview)
