import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QTreeWidgetItem, QVBoxLayout,QWidget
from PySide6.QtWidgets import QDialogButtonBox


from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from plot import Plot
from MyGraphics import plot_graph_smart


from Design.ui_main import Ui_mainWindow
from Design.ui_version import Ui_QVersion
from Design.ui_nml_param import Ui_Nml_param

import json
import lasio


class LasMaster(QMainWindow):
    def __init__(self):
        super(LasMaster, self).__init__()
        # Переменные для хранения данных
        self.curves = None
        self.file_name = None
        self.las = None

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.add_function()

    def add_function(self):
        self.ui.import_p.triggered.connect(self.import_las)
        self.ui.version_p.triggered.connect(self.open_version)
        self.ui.close_p.triggered.connect(self.close)
        self.ui.pb_add_curve.clicked.connect(self.add_curve)
        self.ui.pb_setting_meth.clicked.connect(self.setting_meth)
        self.ui.pb_build.clicked.connect(self.build_plot)

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
        with open("settings.json", 'r') as f:
            curves = json.load(f)

        with open("settings.json", 'w') as f:
            curves.update({curve: self.file_name})
            json.dump(curves, f, indent=4)
        self.curves = QTreeWidgetItem([curve])
        self.ui.tw_curves.addTopLevelItem(self.curves)
        self.curves.setText(1, self.file_name)

        self.ui.qb_curves.clear()

    def setting_meth(self):
        self.nml_param = QDialog()
        self.nml_param.ui = Ui_Nml_param()
        self.nml_param.ui.setupUi(self.nml_param)

        # Загружаем параметры из JSON при открытии диалога
        self.load_param()

        # Подключаем сигналы для кнопок
        self.nml_param.ui.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.save_param)
        self.nml_param.ui.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.nml_param.close)

        self.nml_param.show()

    def save_param(self):
        # Получаем текущие значения параметров из интерфейса
        settings_file = 'settings.json'

        # Загружаем текущие параметры из JSON-файла
        try:
            with open(settings_file, 'r') as f:
                params = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Если файл не найден или пуст, создаем пустой словарь
            params = {}

        # Обновляем только измененные параметры
        params.update({
            "DEEP_MIN": self.nml_param.ui.ds_min.value(),
            "DEEP_MAX": self.nml_param.ui.ds_max.value(),
            "GK_MIN": self.nml_param.ui.ds_gk_min.value(),
            "GK_MAX": self.nml_param.ui.ds_gk_max.value(),
            "DIFF_NML": self.nml_param.ui.ds_diff_nml.value()
        })

        # Сохраняем обновленные параметры обратно в JSON файл
        with open(settings_file, 'w') as f:
            json.dump(params, f, indent=4)

    def load_param(self):
        settings_file = 'settings.json'

        try:
            with open(settings_file, 'r') as f:
                params = json.load(f)

            # Записываем значения в QDoubleSpinBox
            self.nml_param.ui.ds_min.setValue(params.get("DEEP_MIN", 0))
            self.nml_param.ui.ds_max.setValue(params.get("DEEP_MAX", 100))
            self.nml_param.ui.ds_gk_min.setValue(params.get("GK_MIN", 0))
            self.nml_param.ui.ds_gk_max.setValue(params.get("GK_MAX", 100))
            self.nml_param.ui.ds_diff_nml.setValue(params.get("DIFF_NML", 0))


        except FileNotFoundError:
            print(f"Файл {settings_file} не найден")
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON-файла {settings_file}")

    def build_plot(self):
        self.fig = plot_graph_smart()
        self.companovka_for_plot = QVBoxLayout(self.ui.qw_interpret)
        self.ui.verticalLayout.addLayout(self.companovka_for_plot)
        self.canvas = Plot(self.fig)
        self.companovka_for_plot.addWidget(self.canvas)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.companovka_for_plot.addWidget(self.toolbar)





    def open_version(self):
        self.version = QDialog()
        self.version.ui = Ui_QVersion()
        self.version.ui.setupUi(self.version)
        # Считываем версию из JSON
        with open("settings.json", "r") as f:
            self.version.ui.label_4.setText(json.load(f)["VERSION"])
        self.version.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LasMaster = LasMaster()
    LasMaster.show()
    sys.exit(app.exec())
