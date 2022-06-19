import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

#vairables
cutoff = 0.99

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test1.wav')
times = np.arange(len(data))/sampleRate
plt.plot(data, label='data')

#Cutoff
b, a = scipy.signal.butter(3, cutoff)
filtered = scipy.signal.filtfilt(b, a, data)
label = f"{int(cutoff*100):d}%"
plt.plot(filtered, label=label)

#Create The New Wav File
write("C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav", sampleRate, filtered.astype(np.int16));print("Creating New WAV file is Done!")

plt.legend()
plt.show()
