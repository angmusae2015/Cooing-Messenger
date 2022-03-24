from PyQt5.QtWidgets import *


class layout(QHBoxLayout):
    def __init__(self, window):
        super().__init__()

        self.window = window

        self.addStretch(1)

        self.sendButton = QPushButton('문자 보내기', self.window)
        self.sendButton.setFixedHeight(80)
        self.sendButton.setFixedWidth(150)

        self.addWidget(self.sendButton)
