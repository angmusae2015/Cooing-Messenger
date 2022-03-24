from PyQt5.QtWidgets import QHBoxLayout
from . import MsgPreviewLayout
from .MsgSendLayout import MsgSendLayout


class layout(QHBoxLayout):
    def __init__(self, window):
        super().__init__()

        self.window = window

        self.msgSendLayout = MsgSendLayout.layout(self.window)
        self.msgPreviewLayout = MsgPreviewLayout.layout()

        self.addLayout(self.msgSendLayout)
        self.addLayout(self.msgPreviewLayout)
