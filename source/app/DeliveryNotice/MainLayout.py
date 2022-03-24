from PyQt5.QtWidgets import *
from ScheduleTableLayout import ScheduleTableLayout
from MsgLayout import MsgLayout


if __name__ == "__main__":
    app = QApplication([])

    window = QWidget()

    lo = QVBoxLayout()
    lo.addLayout(MsgLayout.layout(window))
    lo.addLayout(ScheduleTableLayout.layout(), 1)
    window.setLayout(lo)

    window.setGeometry(500, 500, 600, 600)
    window.setFixedWidth(600)

    window.show()
    app.exec_()
