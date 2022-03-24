from PyQt5.QtWidgets import QVBoxLayout
from . import SendButtonLayout, ScheduleTableConfigLayout, MsgConfigLayout


class layout(QVBoxLayout):
    def __init__(self, window):
        super().__init__()

        self.window = window

        self.msgConfigLayout = MsgConfigLayout.layout()
        self.scheduleTableConfigLayout = ScheduleTableConfigLayout.layout(self.window)
        self.sendButtonLayout = SendButtonLayout.layout(self.window)

        self.addLayout(self.msgConfigLayout)
        self.addLayout(self.scheduleTableConfigLayout)
        self.addLayout(self.sendButtonLayout)
