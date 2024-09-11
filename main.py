from PySide6.QtWidgets import QApplication,QMainWindow

from ui_main import Ui_mainWindow


class LasMaster(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super(LasMaster, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication([])
    window = LasMaster()
    window.show()
    app.exec()