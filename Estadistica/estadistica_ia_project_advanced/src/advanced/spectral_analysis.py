import numpy as np
from scipy.signal import welch

def compute_fft(series):
    n = len(series)
    fft = np.fft.rfft(series - np.mean(series))
    freqs = np.fft.rfftfreq(n, d=1.0)
    psd = (np.abs(fft)**2) / n
    return freqs, psd

def welch_psd(series, fs=1.0):
    f, Pxx = welch(series, fs=fs, nperseg=min(2048, len(series)))
    return f, Pxx
