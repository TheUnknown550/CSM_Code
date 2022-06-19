#https://swharden.com/blog/2020-09-23-signal-filtering-in-python/
import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test1.wav')
times = np.arange(len(data))/sampleRate

b, a = scipy.signal.butter(3, 0.05, 'lowpass')
filteredLowPass = scipy.signal.filtfilt(b, a, data)

b, a = scipy.signal.butter(3, 0.01, 'highpass')
filteredHighPass = scipy.signal.filtfilt(b, a, data)

b, a = scipy.signal.butter(3, [.01, .5], 'band')
filteredBandPass = scipy.signal.lfilter(b, a, data)

#Create The New Wav File
write("C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav", sampleRate, filteredBandPass.astype(np.int16));print("Creating New WAV file is Done!")

plt.plot(data, label="data")
plt.plot(filteredLowPass, label="Low")
plt.plot(filteredHighPass, label="High")
plt.plot(filteredBandPass, label="band")
plt.legend()
plt.show()