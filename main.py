import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QTreeWidgetItem

from Design.ui_main import Ui_mainWindow
from Design.ui_version import Ui_QVersion
import version as ver
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
        self.ui.close_p.triggered.connect(self.close)
        self.ui.pb_add_curve.clicked.connect(self.add_curve)

    def import_las(self):
        try:
            self.file_name = QFileDialog.getOpenFileName(self, 'Open file', '.', 'las files (*.las)')[0]
            self.las = lasio.read(self.file_name)
            for curve in self.las.curves:
                self.ui.qb_curves.addItem(curve.mnemonic)
        except:
            return

    def add_curve(self):
        curve = self.ui.qb_curves.currentText()

        item = QTreeWidgetItem([curve])
        self.ui.tw_curves.addTopLevelItem(item)

        item.setText(1, self.file_name)
        self.ui.qb_curves.clear()
    def open_version(self):
        self.version = QDialog()
        self.version.ui = Ui_QVersion()
        self.version.ui.setupUi(self.version)
        self.version.ui.label_4.setText(ver.VERSION)
        self.version.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LasMaster = LasMaster()
    LasMaster.show()
    sys.exit(app.exec())
