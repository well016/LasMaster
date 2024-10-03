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
win = pg.GraphicsLayoutWidget(show=True, title="Лог-кривые")
win.resize(800, 600)
win.setWindowTitle('Каротажные кривые')

# Устанавливаем белый фон для всего окна
win.setBackground('white')

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
            scroll_speed = (y_range[1] - y_range[0]) / 0.1  # Скорость прокрутки зависит от масштаба
            self.translateBy(y=scroll_speed / -ev.delta())

# Функция для создания графиков
def create_plot(title, data, color, show_y_axis, min_x=None, max_x=None):
    p = win.addPlot(viewBox=CustomViewBox())  # Используем кастомный ViewBox
    p.setLabels(left='Depth' if show_y_axis else '', top=title)
    p.showGrid(x=True, y=True)  # Включаем сетку по осям X и Y
    p.setDownsampling(mode='peak')
    p.setClipToView(True)

    p.invertY(True)  # Инвертируем ось Y (глубина увеличивается вниз)

    # Убираем ось Y для всех графиков, кроме первого
    if not show_y_axis:
        p.getAxis('left').setStyle(showValues=False)

    # Показываем верхнюю ось X и скрываем нижнюю
    p.showAxis('top', show=True)
    p.hideAxis('bottom')

    # Устанавливаем диапазон по оси X, если указаны min_x и max_x
    if min_x is not None and max_x is not None:
        p.setXRange(min_x, max_x)

    # Создаем кривую
    curve = p.plot(data, common_depth, pen=color)

    # Включаем только вертикальное масштабирование на каждом графике
    p.getViewBox().setMouseEnabled(x=False, y=True)

    # Добавляем к спискам
    plots.append(p)
    curves.append(curve)


# Создаем графики с параметрами min_x и max_x
create_plot("GK_interp", GK_interp, 'r', True, min_x=-10, max_x=10)  # Первый график с осью Y и заданным диапазоном X
create_plot("NML1_interp", NML1_interp, 'g', False, min_x=-2, max_x=2)  # Остальные без оси Y, но с сеткой и диапазоном X
create_plot("NML2_interp", NML2_interp, 'b', False, min_x=-1, max_x=10)
create_plot("NML3_interp", NML3_interp, 'c', False, min_x=-3, max_x=3)
create_plot("DS_interp", DS_interp, 'm', False, min_x=-1.5, max_x=5)

# Связываем только вертикальные оси всех графиков для синхронного масштабирования и прокрутки
for i in range(1, len(plots)):
    plots[i].setYLink(plots[0])  # Связываем вертикальное масштабирование

# Запускаем приложение
if __name__ == '__main__':
    QtWidgets.QApplication.instance().exec_()
