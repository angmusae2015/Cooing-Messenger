from PyQt5.QtWidgets import QApplication, QWidget
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cooing Messenger')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())
