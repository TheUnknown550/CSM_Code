import librosa
import matplotlib.pyplot as plot
import numpy as np
from scipy.signal import find_peaks,butter,hilbert, filtfilt
    
filename = 'c:/Users/matt_c/Documents/Projects/CS-M/Datasets/nwewewe/af/train/(10).wav'

def homomorphic_envelope(y, fs, f_LPF=8, order=3):
    b, a = butter(order, 2 * f_LPF / fs, 'low')#Design the filter
    he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y))))) #Apply the filter to the signal
    return he

y, fs = librosa.load(filename, sr=40000)
he = homomorphic_envelope(y, fs)
peaks, _ = find_peaks(he, height=np.quantile(he,0.8))#detect the highest peaks of the peaks

plot.plot(y)
plot.plot(he, linewidth=2)
plot.plot(peaks, he[peaks], "x")
plot.show()
