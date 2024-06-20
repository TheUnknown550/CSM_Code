import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test1.wav')
times = np.arange(len(data))/sampleRate


# apply a 3-pole lowpass filter at 0.1x Nyquist frequency
b, a = scipy.signal.butter(3, 0.1)

filtered = scipy.signal.filtfilt(b, a, times)
filteredGust = scipy.signal.filtfilt(b, a, times, method="gust")

plt.plot(filteredGust, label="Gustafsson")
plt.plot(data, label="data")
plt.plot(filtered, label="padded")

plt.legend()
plt.title("Padded Data vs. Gustafsson’s Method")
plt.show()