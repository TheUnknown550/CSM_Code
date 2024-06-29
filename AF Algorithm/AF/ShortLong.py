import librosa
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks, butter, hilbert, filtfilt

filename = 'C:/Users/matt_c/Documents/Projects/CS-M/Datasets/10Sec/Normal/(20).wav'

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

peaks, _ = find_peaks(he, height=np.quantile(he, 0.8))  # Detect the highest peaks of the peaks
distance = np.diff(peaks)  # Calculate the distance between the peaks
print("Distance: ", distance)

# locate the short and long distances that shows when is the S1 and S2 sounds are, if the distanecs varies too much then its AF
prev = 0 # record the previous distance
ShortLong = [] # Record the short and long distances Short = 0, Long = 1
for i in distance:
    if i <= prev and prev!= 0:  # Check if the distance is an outlier
        ShortLong.append(0)
    elif i >= prev and prev!= 0:
        ShortLong.append(1)
    prev = i
        
print(ShortLong)

prev = 2 # if the shorts and shorts are together Will add 1 to AF and record the amount of AFs detected
AF = 0
for i in ShortLong:
    if i == prev:
        AF += 1
    else:
        prev = i

print(AF)

plt.plot(y, label='Original Signal')
plt.plot(he, linewidth=2, label='Homomorphic Envelope')
plt.plot(peaks, he[peaks], "x", label='Peaks')
plt.legend()
plt.show()
