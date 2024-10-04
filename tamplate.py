import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets
import numpy as np

# Пример данных
common_depth = np.linspace(0, 1000, 100)  # Пример глубины
GK_interp = np.random.normal(size=100)    # Пример данных для кривой GK_interp
NML1_interp = np.random.normal(size=100)  # Пример данных для кривой NML1_interp
NML2_interp = np.random.normal(size=100)  # Пример данных для кривой NML2_interp
NML3_interp = np.random.normal(size=100)  # Пример данных для кривой NML3_interp
DS_interp = np.random.normal(size=100)    # Пример данных для кривой DS_interp

# Создаем окно приложения
app = QtWidgets.QApplication([])

# Основное окно
win = QtWidgets.QMainWindow()
central_widget = QtWidgets.QWidget()
win.setCentralWidget(central_widget)
layout = QtWidgets.QHBoxLayout(central_widget)
win.setWindowTitle('Каротажные кривые')
win.resize(1000, 600)

# Устанавливаем белый фон для всего окна
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

# Создаем список графиков
plots = []
curves = []

# Класс, наследующий ViewBox, чтобы обработать события масштабирования и прокрутки
class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def wheelEvent(self, ev, axis=None):
        # Проверяем, зажат ли Ctrl. Если да, изменяем масштаб, если нет — прокручиваем
        if ev.modifiers() == QtCore.Qt.ControlModifier:
            # Масштабируем по вертикальной оси, когда зажат Ctrl
            scale_factor = 1.1 if ev.delta() > 0 else 0.9
            self.scaleBy(y=scale_factor)
        else:
            # Прокрутка по вертикальной оси, если Ctrl не зажат
            y_range = self.viewRange()[1]  # Получаем текущий диапазон оси Y
            scroll_speed = (y_range[1] - y_range[0]) / 0.2  # Скорость прокрутки зависит от масштаба
            self.translateBy(y=scroll_speed / -ev.delta())

# Функция для создания графиков

def create_plot(title, data, color, show_y_axis, min_x=None, max_x=None, title_color='blue'):
    splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

    layout.addWidget(splitter)
    plot_widget = pg.PlotWidget(viewBox=CustomViewBox())
    splitter.addWidget(plot_widget)


    plot_widget.setTitle(title, color=title_color)
    plot_widget.showGrid(x=True, y=True)
    plot_widget.setClipToView(True)
    plot_widget.invertY(True)

    # Убираем ось Y для всех графиков, кроме первого
    if not show_y_axis:
        plot_widget.getAxis('left').setStyle(showValues=False)

    # Показываем верхнюю ось X и скрываем нижнюю
    plot_widget.showAxis('top', show=True)
    plot_widget.hideAxis('bottom')

    # Устанавливаем диапазон по оси X, если указаны min_x и max_x
    if min_x is not None and max_x is not None:
        plot_widget.setXRange(min_x, max_x)

    # Включаем только вертикальное масштабирование на каждом графике
    plot_widget.getViewBox().setMouseEnabled(x=False, y=True)

    # Создаем кривую, если переданы данные
    if data is not None:
        curve = plot_widget.plot(data, common_depth, pen=color)
        curves.append(curve)

    # Добавляем к спискам
    plots.append(plot_widget)
    return plot_widget

# Создаем графики
create_plot("GK_interp", GK_interp, 'r', True, min_x=-10, max_x=10, title_color='red')

# Создаем общий график для NML1, NML2 и NML3
nml_plot = create_plot("NML1, NML2, NML3", None, None, False, min_x=-3, max_x=10, title_color='green')
nml_plot.plot(NML1_interp, common_depth, pen='g', name="NML1")
nml_plot.plot(NML2_interp, common_depth, pen='b', name="NML2")
nml_plot.plot(NML3_interp, common_depth, pen='c', name="NML3")

# Создаем график для DS_interp
create_plot("DS_interp", DS_interp, 'm', False, min_x=-1.5, max_x=5, title_color='purple')

# Связываем только вертикальные оси всех графиков для синхронного масштабирования и прокрутки
for i in range(1, len(plots)):
    plots[i].setYLink(plots[0])  # Связываем вертикальное масштабирование

# Запускаем приложение
if __name__ == '__main__':
    win.show()
    QtWidgets.QApplication.instance().exec_()