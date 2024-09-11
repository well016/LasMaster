import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from Design.ui_main import Ui_mainWindow
import lasio


class LasMaster(QMainWindow):
    def __init__(self):
        super(LasMaster, self).__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.add_function()

    def add_function(self):
        self.ui.import_p.triggered.connect(self.import_las)
        self.ui.version_p.triggered.connect(self.import_las)

    def import_las(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Open file', '.', 'las files (*.las)')[0]
            las = lasio.read(file_name)
            print(las)
        except:
            return



if __name__ == "__main__":
    app = QApplication(sys.argv)
    LasMaster = LasMaster()
    LasMaster.show()
    sys.exit(app.exec())
