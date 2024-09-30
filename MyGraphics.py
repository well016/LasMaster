import matplotlib as mpl
import json
import numpy as np
from matplotlib import pyplot as plt
import lasio
from matplotlib.ticker import MaxNLocator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

# Set the backend to Qt for compatibility with PySide6
mpl.use('QtAgg')


def data_reading():
    with open("settings.json", 'r') as f:
        f = json.load(f)
    GK_las = lasio.read(f["GK"])
    NML_las = lasio.read(f["NML1"])
    GK = GK_las['GK']
    NML1 = NML_las['NML1']
    NML2 = NML_las['NML2']
    NML3 = NML_las['NML3']
    DEPTH = GK_las['DEPT']
    min_length = min(len(NML1), len(NML2), len(NML3), len(GK), len(DEPTH))
    NML1 = NML1[:min_length]
    NML2 = NML2[:min_length]
    NML3 = NML3[:min_length]
    DEPTH = DEPTH[:min_length]
    GK = GK[:min_length]
    return GK, NML1, NML2, NML3, DEPTH


def get_analysis_collector():
    GK, NML1, NML2, NML3, DEPTH = data_reading()
    with open("settings.json", 'r') as f:
        f = json.load(f)
    gk_min = f["GK_MIN"]
    gk_max = f["GK_MAX"]
    diff_nml = f["DIFF_NML"]
    diff_1_2 = []
    diff_2_3 = []
    for nml1, nml2 in zip(NML1, NML2):
        diff = round((abs(nml1 - nml2) / (nml1)) * 100, 2)
        diff_1_2.append(diff)
    for nml2, nml3 in zip(NML2, NML3):
        diff = round((abs(nml2 - nml3) / (nml2)) * 100, 2)
        diff_2_3.append(diff)
    collector_status = []
    for i, j in zip(diff_1_2, diff_2_3):
        if i >= diff_nml and j >= diff_nml:
            collector_status.append('Collector')
        else:
            collector_status.append('Not Collector')
    ang=[]
    for gk in GK:
        ag=round((gk-gk_min)/(gk_max-gk_min),3)

        ang.append(ag)

    return collector_status



def plot_graph_smart():
    GK, NML1, NML2, NML3, DEPTH = data_reading()
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 15), dpi=100, facecolor='white',
                                        gridspec_kw={'width_ratios': [1, 1, 0.2]})

    # Пользовательские границы для осей X (минимальные и максимальные значения для растяжения)
    user_min_gk = -1  # Минимальное значение для оси X графика GK
    user_max_gk = 20  # Максимальное значение для оси X графика GK
    user_min_x = -1  # Минимальное значение для оси X графика NML
    user_max_x = 300  # Максимальное значение для оси X графика NML
    print(get_analysis_collector())
    # Устанавливаем начальные пределы осей X на основе пользовательских значений
    ax1.set_xlim(user_min_gk, user_max_gk)
    ax2.set_xlim(user_min_x, user_max_x)

    # Основной график для ax1
    mask_inside_GK = (GK >= user_min_gk) & (GK <= user_max_gk)
    ax1.plot(np.ma.masked_where(~mask_inside_GK, GK), -DEPTH, color='red')

    # Основной график для ax2
    mask_inside_NML1 = (NML1 >= user_min_x) & (NML1 <= user_max_x)
    ax2.plot(np.ma.masked_where(~mask_inside_NML1, NML1), -DEPTH, color='red')

    mask_inside_NML2 = (NML2 >= user_min_x) & (NML2 <= user_max_x)
    ax2.plot(np.ma.masked_where(~mask_inside_NML2, NML2), -DEPTH, color='blue')

    mask_inside_NML3 = (NML3 >= user_min_x) & (NML3 <= user_max_x)
    ax2.plot(np.ma.masked_where(~mask_inside_NML3, NML3), -DEPTH, color='aqua')


    collector_status = get_analysis_collector()
    # Основной график для ax3
    step = 10

    # Adjust the loop to iterate over the depth values with the given step
    for i in range(0, len(DEPTH) - 1, step):
        # Determine the color based on the collector status
        color = 'green' if collector_status[i] == 'Collector' else 'black'

        # Fill between the current and next step depth range
        ax3.fill_betweenx([-DEPTH[i], -DEPTH[min(i + step, len(DEPTH) - 1)]], 0, 1, color=color)

    ax3.set_xlim(0, 1)


    # Переносим линии справа налево как пунктирные линии несколько раз, если они выходят за пределы
    def wrap_lines(values, depth, limit_min, limit_max, ax, color, linestyle):
        shift = (limit_max - limit_min)
        while np.any(values > limit_max):
            excess_values = values > limit_max
            wrapped_values = np.where(excess_values, values - shift, np.nan)
            ax.plot(wrapped_values, -depth, color=color, linestyle=linestyle, linewidth=0.8)
            values = wrapped_values  # обновляем значения для дальнейшего переноса

    # Для графика GK
    wrap_lines(GK, DEPTH, user_min_gk, user_max_gk, ax1, color='red', linestyle=':')

    # Для графика NML1
    wrap_lines(NML1, DEPTH, user_min_x, user_max_x, ax2, color='red', linestyle=':')

    # Для графика NML2
    wrap_lines(NML2, DEPTH, user_min_x, user_max_x, ax2, color='blue', linestyle=':')

    # Для графика NML3
    wrap_lines(NML3, DEPTH, user_min_x, user_max_x, ax2, color='aqua', linestyle=':')

    # Название графиков
    ax1.set_title(f'GK\n{min(GK)}-{max(GK)}', fontsize=8, color='tab:red')
    ax2.text(0.5, 1.065, f'NML1\n{min(NML1)} - {max(NML1)}', ha='center', fontsize=8, color='red',
             transform=ax2.transAxes)
    ax2.text(0.5, 1.035, f'NML2\n{min(NML2)} - {max(NML2)}', ha='center', fontsize=8, color='blue',
             transform=ax2.transAxes)
    ax2.text(0.5, 1.005, f'NML3\n{min(NML3)} - {max(NML3)}', ha='center', fontsize=8, color='aqua',
             transform=ax2.transAxes)
    ax3.set_title(f'\nСтатус\nколлектора', fontsize=8, color='tab:green')

    fig.subplots_adjust(wspace=0)
    y_ticks = np.arange(min(filter(lambda x: x % 10 == 0, -DEPTH)), max(filter(lambda x: x % 10 == 0, -DEPTH)) + 30, 10)

    for ax in [ax1, ax2, ax3]:
        ax.set_yticks(y_ticks)
        ax.set_ylim(min(-DEPTH), max(-DEPTH))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure only integer ticks

    ax1.xaxis.set_ticklabels([])
    ax2.yaxis.set_ticklabels([])
    ax2.xaxis.set_ticklabels([])
    ax3.yaxis.set_ticklabels([])
    ax3.xaxis.set_ticklabels([])

    for ax in [ax1, ax2]:
        ax.grid(True, which='both', linestyle='--', color='gray')
        ax.yaxis.set_ticks_position('none')
        ax.xaxis.set_ticks_position('none')

    ax3.grid(True, axis='y', linestyle='--', color='gray')
    ax3.xaxis.set_ticks_position('none')
    ax3.yaxis.set_ticks_position('none')

    current_grid_interval = 10  # Initial grid interval

    def clamp(value, min_value, max_value):
        return max(min(value, max_value), min_value)

    # Function to handle zooming and scrolling
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

            for ax in [ax1, ax2, ax3]:
                ax.set_ylim(new_ylim)
                ax.set_yticks(np.arange(new_ylim[0], new_ylim[1], current_grid_interval))
                ax.grid(True, which='both', linestyle='--', color='gray')
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure only integer ticks
        else:
            cur_ylim = ax1.get_ylim()
            delta_y = (cur_ylim[1] - cur_ylim[0]) * 0.1

            if event.button == 'down':
                new_ylim = [cur_ylim[0] - delta_y, cur_ylim[1] - delta_y]
            elif event.button == 'up':
                new_ylim = [cur_ylim[0] + delta_y, cur_ylim[1] + delta_y]
            else:
                return

            for ax in [ax1, ax2, ax3]:
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
