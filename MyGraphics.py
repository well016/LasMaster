import matplotlib as mpl
import json
import numpy as np
from matplotlib import pyplot as plt
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
    DEPTH = GK_las['DEPT']
    # Минимальная длина данных
    min_length = min(len(NML1), len(NML2), len(NML3), len(GK), len(DEPTH))
    NML1 = NML1[:min_length]
    NML2 = NML2[:min_length]
    NML3 = NML3[:min_length]
    DEPTH = DEPTH[:min_length]
    GK = GK[:min_length]
    return GK, NML1, NML2, NML3, DEPTH


def plot_graph_smart():
    GK, NML1, NML2, NML3, DEPTH = data_reading()
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=1, ncols=3, figsize=(6, 15), dpi=100, facecolor='white')
    ax1.plot(GK, -DEPTH, color='red')
    ax2.plot(NML1, -DEPTH, color='red')
    ax2.plot(NML2, -DEPTH, color='blue')
    ax2.plot(NML3, -DEPTH, color='aqua')
    ax2.plot()
    ax1.set_title(f'GK\n{min(GK)}-{max(GK)}', fontsize=8,color='tab:red')
    ax2.set_title('')  # Clear the title if already set

    # Add each line of text with different colors
    ax2.text(0.5, 1.055, f'NML1\n{min(NML1)} - {max(NML1)}',ha='center', fontsize=8, color='red',
             transform=ax2.transAxes)
    ax2.text(0.5, 1.03, f'NML2\n{min(NML2)} - {max(NML2)}', ha='center', fontsize=8, color='blue',
             transform=ax2.transAxes)
    ax2.text(0.5, 1.005, f'NML3\n{min(NML3)} - {max(NML3)}', ha='center', fontsize=8, color='aqua',
             transform=ax2.transAxes)

    ax3.set_title(f'\nСтатус\nколлектора', fontsize=8, color='tab:green')
    fig.subplots_adjust(wspace=0)
    y_ticks = np.arange(min(filter(lambda x: x % 10 == 0, -DEPTH)), max(filter(lambda x: x % 10 == 0, -DEPTH))+30, 10)
    for ax in [ax1, ax2, ax3]:
        ax.set_yticks(y_ticks)
        ax.set_ylim(min(-DEPTH), max(-DEPTH))
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

    plt.show()



plot_graph_smart()
