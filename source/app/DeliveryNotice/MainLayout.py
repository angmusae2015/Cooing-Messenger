from PyQt5.QtWidgets import *
from ScheduleTableLayout import ScheduleTableLayout
from MsgLayout import MsgLayout


class layout(QVBoxLayout):
    def __init__(self, window):
        super().__init__()

        self.window = window

        self.msgLayout = MsgLayout.layout(self.window)
        self.scheduleTableLayout = ScheduleTableLayout.layout()

        self.addLayout(self.msgLayout)
        self.addLayout(self.scheduleTableLayout, 1)


if __name__ == "__main__":
    app = QApplication([])

    mainWindow = QWidget()

    lo = layout(mainWindow)
    mainWindow.setLayout(lo)

    mainWindow.setGeometry(500, 500, 600, 600)
    mainWindow.setFixedWidth(600)

    mainWindow.show()
    app.exec_()
