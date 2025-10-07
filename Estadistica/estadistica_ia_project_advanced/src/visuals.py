import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def save_fig(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', dpi=150)
    plt.close(fig)
    return path

def plot_series(x, y, title, xlabel='x', ylabel='y', filename='plot.png'):
    """
    Gráfico de serie simple (línea).
    x, y: arrays o listas.
    """
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(1,1,1)
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return save_fig(fig, filename)

def plot_hist(data, title, bins=100, filename='hist.png'):
    """
    Histograma simple.
    """
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(1,1,1)
    ax.hist(data, bins=bins)
    ax.set_title(title)
    return save_fig(fig, filename)

def plot_scatter(x, y, title, xlabel='x', ylabel='y', filename='scatter.png'):
    """
    Scatter plot.
    """
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x, y, s=4)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return save_fig(fig, filename)
