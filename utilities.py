import matplotlib.pyplot as plt

def pretty_bar_plot(x_values: list, y_values: list, x_label: str, figsize: tuple, label_size:int, ticks_label_size: int) -> plt.figure:
    # https://scentellegher.github.io/visualization/2018/10/10/beautiful-bar-plots-matplotlib.html

    # plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#007acc'
    plt.rcParams['ytick.color']='#007acc'

    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_alpha(0.0)
    plt.hlines(y=y_values, xmin=0, xmax=x_values, color='#007acc', alpha=0.2, linewidth=5)
    plt.plot(x_values, y_values, "o", markersize=5, color='#007acc', alpha=0.6)

    # set labels style
    ax.set_xlabel(x_label, fontsize=label_size, fontweight='bold', color = '#007acc')
    ax.set_ylabel('')

    ax.tick_params(axis='both', labelsize=ticks_label_size)

    # change the style of the axis spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_bounds((0, len(y_values)))
    # add some space between the axis and the plot
    ax.spines['left'].set_position(('outward', 8))
    ax.spines['bottom'].set_position(('outward', 5))
    ax.patch.set_alpha(0.0)

    return fig