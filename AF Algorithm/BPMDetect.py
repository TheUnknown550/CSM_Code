import librosa
from scipy.io import wavfile
import matplotlib.pyplot as plot
import numpy as np
from scipy.signal import savgol_filter, find_peaks,butter,hilbert, filtfilt, correlate
import time

start_time = time.time()

filename = 'c:/Users/matt_c/Documents/Projects/CS-M/Datasets/nwewewe/af/train/(1).wav'

def homomorphic_envelope(y, fs, f_LPF=8, order=3):
    if fs <= 0:
        raise ValueError("Sampling rate (fs) must be greater than zero")
    if f_LPF <= 0 or f_LPF >= fs / 2:
        raise ValueError("Low-pass filter frequency (f_LPF) must be between 0 and fs/2")
    
    b, a = butter(order, 2 * f_LPF / fs, 'low')  # Design the filter
    he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y)))))  # Apply the filter to the signal
    return he

try:# check if file can be read
    fs, y = wavfile.read(filename)  # Load audio
    if y.ndim > 1:  # If stereo, take one channel
        y = y[:, 0]
except Exception as e:
    print(f"Error loading audio file: {e}")
    raise

try:#check if theres an error if not run normally
    he = homomorphic_envelope(y, fs)
except ValueError as e:
    print(f"Error: {e}")
    raise

x = he - np.mean(he)
corr = correlate(x, x, mode='same')
corr = corr[int(corr.size/2):]
min_index = int(0.5*fs)
max_index = int(2*fs)
index = np.argmax(corr[min_index:max_index])
true_index = index+min_index
heartRate = 60/(true_index/fs)

print('Heart Rate: ', heartRate)
print('Time: ', time.time() - start_time)
plot.plot(y)
plot.plot(he, linewidth=2)
plot.show()
