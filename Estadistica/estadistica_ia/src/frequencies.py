import pandas as pd
import numpy as np

def frequency_table(series, bins='auto'):
    if pd.api.types.is_categorical_dtype(series) or series.dtype == object:
        counts = series.value_counts(dropna=False)
        rel = counts / counts.sum()
        return pd.DataFrame({'fi': counts, 'hi': rel})
    counts, edges = np.histogram(series.dropna(), bins=bins)
    mids = (edges[:-1] + edges[1:]) / 2.0
    fi = counts
    Fi = np.cumsum(fi)
    hi = fi / fi.sum()
    Hi = Fi / hi.sum() if hi.sum() != 0 else Fi / fi.sum()
    return pd.DataFrame({'left': edges[:-1], 'right': edges[1:], 'mid': mids, 'fi': fi, 'Fi': Fi, 'hi': hi, 'Hi': Hi})
