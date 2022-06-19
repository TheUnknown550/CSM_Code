import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks
import wave
import sys
import contextlib

audioname = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/Both/B2.wav'
spf = wave.open(audioname, "r")
# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "int16")
fs = spf.getframerate()
Time = np.linspace(0, len(signal) / fs, num=len(signal))

#step2
ab_signal = np.abs(signal)
#step3
signal_filtered = savgol_filter(ab_signal, 4999, 3)
#step4
peaks2, _ = find_peaks(signal_filtered, prominence=250) 


#calculate bpm
with contextlib.closing(wave.open(audioname ,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print('duration= ',duration)
bpm = ((len(peaks2)/2)/duration)*60
print('bpm= ',bpm)

plt.subplot(2, 2, 1)
plt.plot(signal, 'r'); plt.title("1st step")
plt.subplot(2, 2, 2)
plt.plot(ab_signal, 'b'); plt.title("2nd step")
plt.subplot(2, 2, 3)
plt.plot(signal_filtered, 'g'); plt.title("3rd step")
plt.subplot(2, 2, 4)
plt.plot(signal_filtered, 'g'); plt.title("4th step")
plt.plot(peaks2, signal_filtered[peaks2], "ob")
#plt.savefig('Test11.png')
plt.show()