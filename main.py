import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QTreeWidgetItem, QVBoxLayout,QWidget
from PySide6.QtWidgets import QDialogButtonBox,QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import pandas as pd

import MyGraphics
from plot import Plot
from MyGraphics import plot_graph_smart


from Design.ui_main import Ui_mainWindow
from Design.ui_version import Ui_QVersion
from Design.ui_nml_param import Ui_Nml_param

import json
import lasio
import math



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
        self.ui.pb_excel.clicked.connect(self.save_excel)
        self.ui.export_p.triggered.connect(self.save_excel)



    def import_las(self):
        try:
            self.file_name = QFileDialog.getOpenFileName(self, 'Open file', '.', 'las files (*.las)')[0]
            self.las = lasio.read(self.file_name)
            for curve in self.las.curves:
                if curve.mnemonic in ['DS:1,DS1']:
                    curve.mnemonic='DS'
                if curve.mnemonic in ['KPGKS^ED','KPEF']:
                    curve.mnemonic = 'KP'
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
        # Авто подсчет максимального и минимального ГК
        def auto_gk():
            self.nml_param.ui.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.save_param)
            GK, NML1, NML2, NML3, DEPTH, DS, KP = MyGraphics.data_reading()
            gk=[]
            for i, j in zip(GK, DEPTH):
                if j >= self.nml_param.ui.ds_min.value() and j <= self.nml_param.ui.ds_max.value():
                    if not math.isnan(i):
                        gk.append(i)
            gk=sorted(gk)
            self.nml_param.ui.ds_gk_min.setValue(gk[3])
            self.nml_param.ui.ds_gk_max.setValue(gk[-4])
            print(gk)

        # Подключаем сигналы для кнопок
        self.nml_param.ui.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.save_param)
        self.nml_param.ui.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.nml_param.close)
        self.nml_param.ui.pb_auto_gk.clicked.connect(auto_gk)


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
            "DIFF_NML": self.nml_param.ui.ds_diff_nml.value(),
            "a3":self.nml_param.ui.ds_a3.value(),
            "a4":self.nml_param.ui.ds_a4.value(),
            "Kgl":self.nml_param.ui.ds_k.value(),
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
            self.nml_param.ui.ds_a3.setValue(params.get("a3",0))
            self.nml_param.ui.ds_a4.setValue(params.get("a4",0))
            self.nml_param.ui.ds_k.setValue(params.get("Kgl", 0))




        except FileNotFoundError:
            print(f"Файл {settings_file} не найден")
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON-файла {settings_file}")

    def build_plot(self):
        # Check if the layout already exists
        if not hasattr(self, 'companovka_for_plot') or self.companovka_for_plot is None:
            # Initialize the layout if it doesn't exist
            self.companovka_for_plot = QVBoxLayout(self.ui.qw_interpret)
            self.ui.verticalLayout.addLayout(self.companovka_for_plot)
        else:
            # Clear the existing layout's contents
            while self.companovka_for_plot.count():
                item = self.companovka_for_plot.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)  # Remove the widget from its parent

        # Create a new plot and add it to the existing layout
        self.fig = plot_graph_smart()
        self.canvas = Plot(self.fig)
        self.companovka_for_plot.addWidget(self.canvas)

        # Create and add a new toolbar for the updated plot
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.companovka_for_plot.addWidget(self.toolbar)
        self.collector_status_table()

    def group_depths_by_status(self):
        collector_status = MyGraphics.get_analysis_collector()
        GK, NML1, NML2, NML3, DEPTH, DS, KP = MyGraphics.data_reading()
        with open("settings.json", 'r') as file:
            settings = json.load(file)

        depth_min = settings["DEEP_MIN"]
        depth_max = settings["DEEP_MAX"]


        depths= DEPTH
        statuses= collector_status
        intervals = []
        stats = []
        start_depth = depth_min
        current_status = statuses[0]

        for i in range(1, len(depths)):
            if depth_min <= depths[i - 1] <= depth_max:
                if statuses[i] != current_status:
                    end_depth = depths[i - 1]
                    if end_depth - start_depth >= 0.5:
                        intervals.append(f"{start_depth}-{end_depth}м")
                        stats.append(current_status)
                    start_depth = depths[i]
                    current_status = statuses[i]

        # Добавление последнего интервала


        end_depth = depth_max
        if end_depth - start_depth >= 0.5:
            intervals.append(f"{start_depth}-{end_depth} м")
            stats.append(current_status)

        return intervals, stats

    def collector_status_table(self):
        depths, statuses= self.group_depths_by_status()

        # Combine the lists into a single data structure
        data = list(zip(depths, statuses))


        # Create the model
        model = QStandardItemModel(len(data), 2)  # Number of rows, Number of columns
        model.setHorizontalHeaderLabels(["Интервал глубин,м", "Статус коллектора"])

        # Populate the model with data from the combined lists
        for row, (depth, status) in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(depth)))  # Set the depth in the first column
            model.setItem(row, 1, QStandardItem(str(status)))  # Set the status in the second column

        # Set the model to the QTableView
        self.ui.qv_table_status.setModel(model)

        # Hide the row numbering (vertical header)
        self.ui.qv_table_status.verticalHeader().setVisible(False)

        # Make the columns resize based on the window size
        self.ui.qv_table_status.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def open_version(self):
        self.version = QDialog()
        self.version.ui = Ui_QVersion()
        self.version.ui.setupUi(self.version)
        # Считываем версию из JSON
        with open("settings.json", "r") as f:
            self.version.ui.label_4.setText(json.load(f)["VERSION"])
        self.version.show()


    def save_excel(self):
        DEPTH, collector_status= self.group_depths_by_status()

        data = {
            "Интервал глубин,м": DEPTH,
            "Статус Коллектора": collector_status
        }

        df = pd.DataFrame(data)
        # Открытие диалогового окна для выбора пути сохранения
        app = QApplication.instance()  # Проверка, запущен ли уже экземпляр QApplication
        if app is None:
            app = QApplication([])
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Сохранить файл как", "",
                                                   "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_path:  # Если пользователь выбрал путь
            if not file_path.endswith(".xlsx"):
                file_path += ".xlsx"
            df.to_excel(file_path, index=False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    LasMaster = LasMaster()
    LasMaster.show()
    sys.exit(app.exec())
