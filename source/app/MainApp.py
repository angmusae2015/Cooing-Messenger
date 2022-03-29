from PyQt5.QtWidgets import *
from DeliveryNotice import DeliveryNoticeMain


if __name__ == "__main__":
    app = QApplication([])

    mainWindow = QWidget()

    mainWindow.setLayout(DeliveryNoticeMain.layout(mainWindow))

    # mainWindow.setGeometry(500, 500, 600, 600)
    mainWindow.setFixedWidth(350)

    mainWindow.show()
    app.exec_()
