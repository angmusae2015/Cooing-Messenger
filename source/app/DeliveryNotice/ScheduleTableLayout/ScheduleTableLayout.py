from PyQt5.QtWidgets import QVBoxLayout, QTableWidget


class layout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.scheduleTable = QTableWidget(30, 5)
        self.addWidget(self.scheduleTable)
