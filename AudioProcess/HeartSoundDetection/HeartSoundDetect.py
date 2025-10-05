# Imports
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter,hilbert, filtfilt,correlate, find_peaks
from scipy.io import wavfile

# Variables
S1 = []
S2 = []

# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])
    print('Trimmed File Complete')

#Load Audio
filename = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/AmpLowTests/normal/AmpToLow/LowAudio/(1).wav'
trim_wav(filename,0,10)

# BPM Counter
# Load audio
y, fs = librosa.load('File.wav')

# Apply Adaptive Threasholding
b, a = butter(4, 2 * 8 / fs, 'low')
he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y)))))
print('Adaptive Threasholding Complete')
print(he)

# Calculate BPM
x = he - np.mean(he)
corr = correlate(x, x, mode='same')  
corr = corr[int(corr.size/2):]
min_index = int(0.5*fs)
max_index = int(2*fs)
index = np.argmax(corr[min_index:max_index])
true_index = index+min_index
BPM = 60/(true_index/fs)
print('BPM Calculate Complete')
print('BPM: ',BPM)

# Find peaks
height = np.mean(he)

peaks, _ = find_peaks(he, height=height)
print(peaks)
print(he[peaks])

# Find S1 and S2 of sound
for i in range(len(peaks)):
    if (i+3) <= len(peaks):
        
        # Finding space between each beat
        space1 = he[peaks[i+1]] - he[peaks[i]]
        space2 = he[peaks[i+2]] - he[peaks[i+1]]

        # Detecting S1/S2
        if space1 >= space2:
            S2.append(peaks[i])
        else:
            S1.append(peaks[i])
    elif (i+2)<=len(peaks):
        if peaks[i-1] == S2[len(S2)-1]:
            S1.append(peaks[i])
            S2.append(peaks[i+1])
        elif peaks[i-1] == S1[len(S1)-1]:
            S2.append(peaks[i])
            S1.append(peaks[i+1])
        


#Plot graph
plt.title('Sound Graph')
plt.xlabel('Time')
plt.ylabel('Amplitude')
bbox_props = dict(boxstyle="round", fc="white", ec="black", lw=0.5, alpha=0.5)
plt.text(0.95, 0.95, f'BPM: {BPM:.2f}', transform=plt.gca().transAxes,
         fontsize=14, verticalalignment='top', horizontalalignment='right',
         bbox=bbox_props)
plt.plot(y, label='Sound')
plt.plot(he, linewidth=2, label='Adaptive Threasholding')
plt.plot(S1, he[S1],'ro', label='S1', color='g')
plt.plot(S2, he[S2],'ro', label='S2', color='r')
plt.legend()
plt.show()