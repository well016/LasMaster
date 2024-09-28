import matplotlib as mpl
import json
import numpy as np
from matplotlib import pyplot as plt
import lasio
from matplotlib.ticker import MaxNLocator

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


def plot_graph_smart():
    GK, NML1, NML2, NML3, DEPTH = data_reading()
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(6, 15), dpi=100, facecolor='white',width_ratios=[1, 1, 0.2])

    ax1.plot(GK, -DEPTH, color='red')
    ax2.plot(NML1, -DEPTH, color='red')
    ax2.plot(NML2, -DEPTH, color='blue')
    ax2.plot(NML3, -DEPTH, color='aqua')

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

        # Check if the mouse is over any of the axes
        if event.inaxes is None:
            return

        # Handle zooming when Ctrl is pressed
        if event.key == 'control':
            cur_ylim = ax1.get_ylim()
            ydata = event.ydata

            if event.button == 'up':
                scale_factor = 1 / base_scale
                current_grid_interval /= base_scale  # Decrease grid interval
            elif event.button == 'down':
                scale_factor = base_scale
                current_grid_interval *= base_scale  # Increase grid interval
            else:
                scale_factor = 1

            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
            rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

            new_ylim = [ydata - new_height * (1 - rely), ydata + new_height * rely]

            # Clamp the grid interval to be between 1 and 10 and ensure it is a whole number
            current_grid_interval = clamp(round(current_grid_interval), 0.1, 10)

            # Update y-limits and grid intervals for all axes
            for ax in [ax1, ax2, ax3]:
                ax.set_ylim(new_ylim)
                ax.set_yticks(np.arange(new_ylim[0], new_ylim[1], current_grid_interval))
                ax.grid(True, which='both', linestyle='--', color='gray')
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure only integer ticks

        # Handle regular scrolling (without Ctrl) - only change the view, not the grid
        else:
            cur_ylim = ax1.get_ylim()
            delta_y = (cur_ylim[1] - cur_ylim[0]) * 0.1

            if event.button == 'down':
                new_ylim = [cur_ylim[0] - delta_y, cur_ylim[1] - delta_y]
            elif event.button == 'up':
                new_ylim = [cur_ylim[0] + delta_y, cur_ylim[1] + delta_y]
            else:
                return

            # Update y-limits without changing the grid
            for ax in [ax1, ax2, ax3]:
                ax.set_ylim(new_ylim)
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure only integer ticks

        fig.canvas.draw_idle()

    # Capture the scroll event
    fig.canvas.mpl_connect('scroll_event', zoom)

    plt.show()


plot_graph_smart()
