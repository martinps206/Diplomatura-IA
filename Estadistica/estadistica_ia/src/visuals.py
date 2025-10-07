import matplotlib.pyplot as plt
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_fig(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', dpi=150)
    plt.close(fig)
    return path

def hist_plot(series, bins=50, filename='hist.png', density=False):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hist(series.dropna(), bins=bins, density=density)
    ax.set_title('Histograma')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frecuencia' if not density else 'Densidad')
    return save_fig(fig, filename)

def ecdf_plot(series, filename='ecdf.png'):
    x = np.sort(series.dropna())
    y = np.arange(1, len(x)+1) / len(x)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.step(x, y)
    ax.set_title('ECDF')
    ax.set_xlabel('Valor')
    ax.set_ylabel('F(x) acumulada')
    return save_fig(fig, filename)

def qq_plot(series, filename='qq.png'):
    from scipy import stats
    x = series.dropna()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    stats.probplot(x, dist='norm', plot=ax)
    ax.set_title('Q-Q plot vs Normal')
    return save_fig(fig, filename)

def boxplot_by(series, by, filename='boxplot.png'):
    import numpy as np
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(1,1,1)
    groups = [series[by==k].dropna().values for k in np.unique(by)]
    ax.boxplot(groups, labels=[str(k) for k in np.unique(by)])
    ax.set_title('Boxplots por grupo')
    return save_fig(fig, filename)
