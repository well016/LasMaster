import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog,QDialog

from Design.ui_main import Ui_mainWindow
from Design.ui_version import Ui_QVersion
import lasio


class LasMaster(QMainWindow):
    def __init__(self):
        super(LasMaster, self).__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.add_function()

    def add_function(self):
        self.ui.import_p.triggered.connect(self.import_las)
        self.ui.version_p.triggered.connect(self.open_version)

    def import_las(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Open file', '.', 'las files (*.las)')[0]
            las = lasio.read(file_name)
            print(las)
        except:
            return
    def open_version(self):
        self.version = QDialog()
        self.version.ui = Ui_QVersion()
        self.version.ui.setupUi(self.version)
        self.version.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    LasMaster = LasMaster()
    LasMaster.show()
    sys.exit(app.exec())
