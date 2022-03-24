from PyQt5.QtWidgets import QVBoxLayout
from . import SendButtonLayout, ScheduleTableConfigLayout, MsgConfigLayout


class layout(QVBoxLayout):
    def __init__(self, parent):
        super().__init__()

        self.msgConfigLayout = MsgConfigLayout.layout()
        self.scheduleTableConfigLayout = ScheduleTableConfigLayout.layout(parent)
        self.sendButtonLayout = SendButtonLayout.layout(parent)

        self.addLayout(self.msgConfigLayout)
        self.addLayout(self.scheduleTableConfigLayout)
        self.addLayout(self.sendButtonLayout)
