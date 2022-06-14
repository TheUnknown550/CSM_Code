import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

FileName = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/.wav'

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read(FileName)
times = np.arange(len(data))/sampleRate

# create a normalized Hanning window
windowSize = 300
window = np.hanning(windowSize)
window = window / window.sum()

# filter the data using convolution
filtered = np.convolve(window, data, mode='valid')


plt.plot(data, label='Original')
#plt.plot(times ,filteredLowPass, label='LowFiltered')
#plt.plot(times, filteredHighPass, label='HighFiltered')
plt.plot(filtered, label='Filtered')

plt.legend()
plt.show()