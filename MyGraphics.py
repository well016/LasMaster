import matplotlib as mpl
import json
import numpy as np
from matplotlib import pyplot as plt
import lasio
from matplotlib.ticker import MaxNLocator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
import math
import matplotlib.collections as mc
import time


# Set the backend to Qt for compatibility with PySide6
mpl.use('QtAgg')

## Декоратор для подсчета времени выполнения функции
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

def data_reading():
    with open("settings.json", 'r') as f:
        f = json.load(f)
    GK_las = lasio.read(f["GK"])
    NML_las = lasio.read(f["NML1"])
    DS_las=lasio.read(f["DS"])
    GK = GK_las['GK']
    NML1 = NML_las['NML1']
    NML2 = NML_las['NML2']
    NML3 = NML_las['NML3']
    try:
        DEPTH_GK = GK_las['DEPT']
    except:
        DEPTH_GK = GK_las['DEPTH']
    try:
        DEPTH_NML = NML_las['DEPT']
    except:
        DEPTH_NML = NML_las['DEPTH']

    try:
        DS = NML_las['DS']
    except:
        try:
            DS = NML_las['DS:1']
        except:
            DS = DS_las['DS']
    if max(DS)<1:
        DS=DS*1000
    # Общая глубина - объединение глубин GK и NML
    common_depth = np.union1d(DEPTH_GK, DEPTH_NML)

    # Интерполяция данных по общим глубинам
    GK_interp = np.interp(common_depth, DEPTH_GK, GK)
    NML1_interp = np.interp(common_depth, DEPTH_NML, NML1)
    NML2_interp = np.interp(common_depth, DEPTH_NML, NML2)
    NML3_interp = np.interp(common_depth, DEPTH_NML, NML3)
    DS_interp = np.interp(common_depth, DEPTH_NML, DS)

    return GK_interp, NML1_interp, NML2_interp, NML3_interp, common_depth, DS_interp

@time_it
def get_analysis_collector():
    GK, NML1, NML2, NML3, DEPTH, DS = data_reading()
    with open("settings.json", 'r') as f:
        f = json.load(f)
    gk_min = f["GK_MIN"]
    gk_max = f["GK_MAX"]
    diff_nml = f["DIFF_NML"]
    a3=f['a3']
    a4=f['a4']
    kgl=f['Kgl']
    diff_1_2 = []
    diff_2_3 = []
    for nml1, nml2 in zip(NML1, NML2):
        diff = round((abs(nml1 - nml2) / (nml1)) * 100, 2)
        diff_1_2.append(diff)
    for nml2, nml3 in zip(NML2, NML3):
        diff = round((abs(nml2 - nml3) / (nml2)) * 100, 2)
        diff_2_3.append(diff)
    ang = []
    lkgl = []
    for gk in GK:
        ag = round((gk - gk_min) / (gk_max - gk_min), 3)
        ang.append(ag)
    for i in ang:
        d = a3 * i ** a4
        lkgl.append(d)
    collector_status = []
    for i, j, k in zip(diff_1_2, diff_2_3,lkgl):
        if i >= diff_nml and j >= diff_nml and k<kgl:
            collector_status.append('Collector')
        else:
            collector_status.append('Not Collector')



    return collector_status


@time_it
def plot_graph_smart():
    GK, NML1, NML2, NML3, DEPTH, DS = data_reading()
    fig, (ax1, ax4, ax2, ax3) = plt.subplots(nrows=1, ncols=4, figsize=(8, 15), dpi=100, facecolor='white',
                                             gridspec_kw={'width_ratios': [1, 0.4, 1, 0.2]})

    # Пользовательские границы для осей X (минимальные и максимальные значения для растяжения)
    user_min_gk = 0  # Минимальное значение для оси X графика GK
    user_max_gk = 20  # Максимальное значение для оси X графика GK
    user_min_x = 0  # Минимальное значение для оси X графика NML
    user_max_x = 200  # Максимальное значение для оси X графика NML
    user_min_ds= 200 # Минимальное значение для оси X графика DS
    user_max_ds = 300 # Максимальное значение для оси X графика DS

    # Устанавливаем начальные пределы осей X на основе пользовательских значений
    ax1.set_xlim(user_min_gk, user_max_gk)
    ax2.set_xlim(user_min_x, user_max_x)
    ax4.set_xlim(user_min_ds, user_max_ds)

    # Основной график для ax1


    ax1.plot(GK, -DEPTH, color='red')


    # Основной график для ax4
    ax4.plot(DS, -DEPTH, color='green')

    # Основной график для ax2
    ax2.plot(NML1, -DEPTH, color='red')
    ax2.plot(NML2, -DEPTH, color='blue')
    ax2.plot(NML3, -DEPTH, color='aqua')

    collector_status = get_analysis_collector()

    with open("settings.json", 'r') as file:
        settings = json.load(file)

    depth_min = -settings["DEEP_MIN"]
    depth_max = -settings["DEEP_MAX"]
    depth_values = np.array(DEPTH)
    collector_status = np.array(collector_status)

    depth_start = -depth_values[:-1]
    depth_end = -depth_values[1:]

    mask = (depth_start > depth_max) & (depth_end < depth_min)
    filtered_indices = np.where(mask)[0]
    filtered_depth_start = depth_start[filtered_indices]
    filtered_depth_end = depth_end[filtered_indices]
    filtered_collector_status = collector_status[filtered_indices]

    segments = []
    colors = []
    for start, end, status in zip(filtered_depth_start, filtered_depth_end, filtered_collector_status):
        segments.append([(0, start), (1, start), (1, end), (0, end)])
        colors.append('green' if status == 'Collector' else 'black')

    poly_collection = mc.PolyCollection(segments, facecolors=colors, edgecolors='none')
    ax3.add_collection(poly_collection)
    ax3.set_xlim(0, 1)
    ax3.autoscale_view()


    # Переносим линии справа налево как пунктирные линии несколько раз, если они выходят за пределы
    def wrap_lines(values, depth, limit_min, limit_max, ax, color, linestyle):
        shift = (limit_max - limit_min)
        while np.any(values > limit_max):
            excess_values = values >= limit_max
            wrapped_values = np.where(excess_values, values - shift, limit_min-0.1)
            ax.plot(wrapped_values, -depth, color=color, linestyle=linestyle, linewidth=0.8)
            values = wrapped_values  # обновляем значения для дальнейшего переноса

    # Для графика GK
    wrap_lines(GK, DEPTH, user_min_gk, user_max_gk, ax1, color='red', linestyle=':')

    wrap_lines(DS, DEPTH, user_min_ds, user_max_ds, ax4, color='green', linestyle=':')

    # Для графика NML1
    wrap_lines(NML1, DEPTH, user_min_x, user_max_x, ax2, color='red', linestyle=':')

    # Для графика NML2
    wrap_lines(NML2, DEPTH, user_min_x, user_max_x, ax2, color='blue', linestyle=':')

    # Для графика NML3
    wrap_lines(NML3, DEPTH, user_min_x, user_max_x, ax2, color='aqua', linestyle=':')

    # Название графиков
    ax1.set_title(f'GK, ur/h\n{min((filter(lambda x: not math.isnan(x), GK)))}-'
                  f'{max(filter(lambda x: not math.isnan(x), GK))}', fontsize=8, color='red')
    ax4.set_title(f'DS, мм\n{round(min((filter(lambda x: not math.isnan(x), DS))), 1)} - '
                  f'{round(max((filter(lambda x: not math.isnan(x), DS))), 1)}', fontsize=8, color='green')
    ax2.text(0.5, 1.095, f'NML1\n{min((filter(lambda x: not math.isnan(x), NML1)))} - '
                        f'{max((filter(lambda x: not math.isnan(x), NML1)))}', ha='center', fontsize=8, color='red',
             transform=ax2.transAxes)
    ax2.text(0.5, 1.065, f'NML2\n{min((filter(lambda x: not math.isnan(x), NML2)))} - '
                        f'{max((filter(lambda x: not math.isnan(x), NML2)))}', ha='center', fontsize=8, color='blue',
             transform=ax2.transAxes)
    ax2.text(0.5, 1.035, f'NML3\n{min((filter(lambda x: not math.isnan(x), NML3)))} - '
                         f'{max((filter(lambda x: not math.isnan(x), NML3)))}', ha='center', fontsize=8, color='aqua',
             transform=ax2.transAxes)
    ax3.set_title(f'\nСтатус\nколлектора', fontsize=8, color='green')

    fig.subplots_adjust(wspace=0)
    y_ticks = np.arange(min(filter(lambda x: x % 10 == 0, -DEPTH)), max(filter(lambda x: x % 10 == 0, -DEPTH)) + 30, 10)

    for ax in [ax1, ax2, ax3,ax4]:
        ax.set_yticks(y_ticks)
        ax.set_ylim(min(-DEPTH), max(-DEPTH))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure only integer ticks
    # Убираем шкалу по х и y

    ax2.yaxis.set_ticklabels([])
    ax3.yaxis.set_ticklabels([])
    ax3.xaxis.set_ticklabels([])

    ax4.yaxis.set_ticklabels([])
    # Добавил шкалу по х с параметрами
    ax4.xaxis.set_ticks_position('top')
    ax4.tick_params(axis='x', labelsize=7)

    ax2.xaxis.set_ticks_position('top')
    ax4.tick_params(axis='x', labelsize=7)

    ax1.xaxis.set_ticks_position('top')
    ax4.tick_params(axis='x', labelsize=7)

    ax1.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both',nbins=4))
    ax2.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both',nbins=4))
    ax4.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both',nbins=4))




    for ax in [ax1, ax2,ax4]:
        ax.grid(True, which='both', linestyle='--', color='gray')
        ax.yaxis.set_ticks_position('none')
        ax.xaxis.set_ticks_position('none')

    ax3.grid(True, axis='y', linestyle='--', color='gray')
    ax3.xaxis.set_ticks_position('none')
    ax3.yaxis.set_ticks_position('none')

    ax4.grid(True, axis='y', linestyle='--', color='gray')
    ax4.xaxis.set_ticks_position('none')
    ax4.yaxis.set_ticks_position('none')




    current_grid_interval = 10  # Initial grid interval

    def clamp(value, min_value, max_value):
        return max(min(value, max_value), min_value)

    # Function to handle zooming and scrolling
    @time_it
    def zoom(event):
        nonlocal current_grid_interval
        base_scale = 1.1

        if event.inaxes is None:
            return
        # print(f"Zoom event: {event}, key: {event.key}, button: {event.button}")
        # Handle zooming when Ctrl is pressed
        modifiers = QApplication.keyboardModifiers()  # Проверяем, какие модификаторы клавиш активны

        # Проверяем, что нажат Ctrl
        if modifiers == Qt.ControlModifier:
            # print("Ctrl key is pressed")
            cur_ylim = ax1.get_ylim()
            cur_xlim1 = ax1.get_xlim()
            cur_xlim2 = ax2.get_xlim()
            xdata = event.xdata
            ydata = event.ydata

            if event.button == 'up':
                scale_factor = 1 / base_scale
                current_grid_interval /= base_scale
            elif event.button == 'down':
                scale_factor = base_scale
                current_grid_interval *= base_scale
            else:
                scale_factor = 1

            # Adjusting y-axis limits
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
            rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])
            new_ylim = [ydata - new_height * (1 - rely), ydata + new_height * rely]

            # Updating grid intervals and limits
            current_grid_interval = clamp(round(current_grid_interval), 0.1, 10)

            for ax in [ax1, ax4, ax2, ax3]:
                ax.set_ylim(new_ylim)
                ax.set_yticks(np.arange(new_ylim[0], new_ylim[1], current_grid_interval))
                ax.grid(True, which='both', linestyle='--', color='gray')
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))
                # Ensure only integer ticks
        else:
            cur_ylim = ax1.get_ylim()
            delta_y = (cur_ylim[1] - cur_ylim[0]) * 0.1

            if event.button == 'down':
                new_ylim = [cur_ylim[0] - delta_y, cur_ylim[1] - delta_y]
            elif event.button == 'up':
                new_ylim = [cur_ylim[0] + delta_y, cur_ylim[1] + delta_y]
            else:
                return

            for ax in [ax1, ax4, ax2, ax3]:
                ax.set_ylim(new_ylim)
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('scroll_event', zoom)
    print('График построен успешно')

    # plt.show()
    return fig


if __name__ == '__main__':
    plot_graph_smart()
    plt.show()
