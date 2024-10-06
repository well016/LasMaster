import sys  # Импортируем модуль sys, чтобы взаимодействовать с системными параметрами и аргументами командной строки
import pyqtgraph as pg  # Импортируем pyqtgraph, библиотеку для построения графиков
from pyqtgraph.Qt import QtCore, QtWidgets # Импортируем QtCore и QtWidgets из pyqtgraph для работы с элементами интерфейса
import numpy as np  # Импортируем numpy, библиотеку для работы с массивами и научными вычислениями
import json
import lasio

def data_reading():
    with open("settings.json", 'r') as f:
        f = json.load(f)
    GK_las = lasio.read(f["GK"])
    NML_las = lasio.read(f["NML1"])
    GK = GK_las['GK']
    NML1 = NML_las['NML1']
    NML2 = NML_las['NML2']
    NML3 = NML_las['NML3']
    DEPTH_GK = GK_las['DEPT']
    DEPTH_NML = NML_las['DEPT']
    try:
        DS = NML_las['DS']
    except:
        DS = NML_las['DS:1']

    # Общая глубина - объединение глубин GK и NML
    common_depth = np.union1d(DEPTH_GK, DEPTH_NML)

    # Интерполяция данных по общим глубинам
    GK_interp = np.interp(common_depth, DEPTH_GK, GK)
    NML1_interp = np.interp(common_depth, DEPTH_NML, NML1)
    NML2_interp = np.interp(common_depth, DEPTH_NML, NML2)
    NML3_interp = np.interp(common_depth, DEPTH_NML, NML3)
    DS_interp = np.interp(common_depth, DEPTH_NML, DS)

    return GK_interp, NML1_interp, NML2_interp, NML3_interp, common_depth, DS_interp

GK_interp, NML1_interp, NML2_interp, NML3_interp, common_depth, DS_interp = data_reading()

# Создаем окно приложения
app = QtWidgets.QApplication([])  # Создаем экземпляр приложения Qt

# Основное окно
win = QtWidgets.QMainWindow()  # Создаем главное окно
central_widget = QtWidgets.QWidget()  # Создаем центральный виджет для главного окна
win.setCentralWidget(central_widget)  # Устанавливаем центральный виджет в главное окно
layout = QtWidgets.QVBoxLayout(central_widget)# Устанавливаем вертикальный лэйаут в центральный виджет

win.setWindowTitle('Каротажные кривые')  # Устанавливаем заголовок окна
win.resize(1000, 600)  # Устанавливаем размер окна 1000x600 пикселей

# Устанавливаем белый фон для всего окна
pg.setConfigOption('background', 'w')  # Устанавливаем белый фон для графиков

# Создаем QSplitter для размещения графиков
splitter = QtWidgets.QSplitter()  # Создаем горизонтальный QSplitter для размещения графиков
scroll=QtWidgets.QScrollBar(QtCore.Qt.Horizontal)
layout.addWidget(splitter)
layout.addWidget(scroll)
scroll.setFixedHeight(15)



  # Добавляем QSplitter в лэйаут


# Список графиков и кривых
plots = []  # Создаем пустой список для хранения графиков
curves_data = []  # Список для хранения данных о кривых

# Класс, наследующий ViewBox, чтобы обработать события масштабирования и прокрутки
class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Инициализируем родительский класс

    def wheelEvent(self, ev, axis=None):
        # Проверяем, зажат ли Ctrl. Если да, изменяем масштаб, если нет — прокручиваем
        if ev.modifiers() == QtCore.Qt.ControlModifier:  # Если зажат Ctrl
            scale_factor = 1.1 if ev.delta() > 0 else 0.9  # Определяем коэффициент масштабирования
            self.scaleBy(y=scale_factor)  # Масштабируем по вертикальной оси
        else:
            y_range = self.viewRange()[1]  # Получаем текущий диапазон оси Y
            scroll_speed = (y_range[1] - y_range[0]) / 0.05  # Определяем скорость прокрутки
            self.translateBy(y=scroll_speed / -ev.delta())  # Прокручиваем по вертикали

# Функция для создания графиков
def create_plot(title, show_y_axis=False, min_x=None, max_x=None, title_color='black'):
    plot_widget = pg.PlotWidget(viewBox=CustomViewBox()) # Создаем экземпляр PlotWidget с CustomViewBox
     # Устанавливаем размер графика
    splitter.addWidget(plot_widget)  # Добавляем график в QSplitter
    plot_widget.setTitle(title, color=title_color)  # Устанавливаем заголовок графика и его цвет
    plot_widget.showGrid(x=True, y=True)  # Включаем отображение сетки по осям X и Y
    plot_widget.invertY(True)  # Инвертируем ось Y

    # Убираем ось Y для всех графиков, кроме первого
    if not show_y_axis:
        plot_widget.getAxis('left').setStyle(showValues=False)  # Скрываем значения оси Y

    # Показываем верхнюю ось X и скрываем нижнюю
    plot_widget.showAxis('top', show=True)  # Показываем верхнюю ось X
    plot_widget.hideAxis('bottom')  # Скрываем нижнюю ось X

    # Устанавливаем диапазон по оси X, если указаны min_x и max_x
    if min_x is not None and max_x is not None:
        plot_widget.setXRange(min_x, max_x)  # Устанавливаем диапазон оси X

    # Включаем только вертикальное масштабирование на каждом графике
    plot_widget.getViewBox().setMouseEnabled(x=False, y=True)  # Включаем вертикальное масштабирование

    plots.append(plot_widget)  # Добавляем график в список графиков
    return plot_widget  # Возвращаем график

# Функция для добавления кривых в график
def add_curve(plot_widget, data, depth, color='b', width=3, style=None):
    pen = pg.mkPen(color=color, width=width, style=style)  # Создаем перо для кривой
    plot_widget.plot(data, depth, pen=pen)  # Добавляем кривую на график
    curves_data.append({'plot': plot_widget, 'data': data, 'depth': depth, 'color': color, 'width': width, 'style': style})

# Создаем графики и добавляем кривые
plot_gk = create_plot("GK_interp", show_y_axis=True, min_x=0, max_x=300, title_color='red')
add_curve(plot_gk, GK_interp, common_depth, color='red', width=3)
add_curve(plot_gk, DS_interp, common_depth, color='green', width=3, style=QtCore.Qt.DashLine)

nml_plot = create_plot("NML1, NML2, NML3", min_x=0, max_x=200, title_color='green')
add_curve(nml_plot, NML1_interp, common_depth, color='red')
add_curve(nml_plot, NML2_interp, common_depth, color='blue')
add_curve(nml_plot, NML3_interp, common_depth, color='aqua')

plot_ds= create_plot("DS", min_x=200, max_x=400, title_color='blue')
add_curve(plot_ds, DS_interp, common_depth, color='green')




# Связываем только вертикальные оси всех графиков для синхронного масштабирования и прокрутки
for i in range(1, len(plots)):
    plots[i].setYLink(plots[0])  # Связываем вертикальное масштабирование всех графиков с первым

# Запускаем приложение
if __name__ == '__main__':
    win.show()  # Показываем главное окно
    QtWidgets.QApplication.instance().exec()  # Запускаем главный цикл приложения