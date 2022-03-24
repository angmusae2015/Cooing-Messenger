from PyQt5.QtWidgets import QHBoxLayout
from . import MsgPreviewLayout
from .MsgSendLayout import MsgSendLayout


class layout(QHBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.msgSendLayout = MsgSendLayout.layout(parent)
        self.msgPreviewLayout = MsgPreviewLayout.layout()

        self.addLayout(self.msgSendLayout)
        self.addLayout(self.msgPreviewLayout)
