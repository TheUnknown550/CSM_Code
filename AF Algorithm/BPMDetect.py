import librosa
import matplotlib.pyplot as plot
import numpy as np
from scipy.signal import savgol_filter, find_peaks,butter,hilbert, filtfilt, correlate
    
filename = 'c:/Users/matt_c/Documents/Projects/CS-M/Datasets/nwewewe/af/train/127_1306764300147_C2.wav'

def homomorphic_envelope(y, fs, f_LPF=8, order=3):
    b, a = butter(order, 2 * f_LPF / fs, 'low')
    he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y)))))
    return he

print('heartrate start!')
y, fs = librosa.load(filename, sr=40000)
he = homomorphic_envelope(y, fs)
x = he - np.mean(he)
corr = correlate(x, x, mode='same')
corr = corr[int(corr.size/2):]
min_index = int(0.5*fs)
max_index = int(2*fs)
index = np.argmax(corr[min_index:max_index])
true_index = index+min_index
heartRate = 60/(true_index/fs)

print('Heart Rate: ', heartRate)
plot.plot(y)
plot.plot(he, linewidth=2)
plot.show()
