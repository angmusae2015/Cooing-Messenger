from PyQt5.QtWidgets import *


class layout(QHBoxLayout):
    def __init__(self, parent):
        super().__init__()

        self.addStretch(1)

        self.sendButton = QPushButton('문자 보내기', parent)
        self.sendButton.setFixedHeight(80)
        self.sendButton.setFixedWidth(150)

        self.addWidget(self.sendButton)
