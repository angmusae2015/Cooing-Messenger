from PyQt5.QtWidgets import QVBoxLayout, QTableWidget
from openpyxl import load_workbook
import re


class layout(QVBoxLayout):
    def __init__(self, window):
        super().__init__()

        self.window = window

        self.scheduleTable = QTableWidget()
        self.addWidget(self.scheduleTable)
