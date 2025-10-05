# Imports
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter,hilbert, filtfilt,correlate
from scipy.io import wavfile


# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])
    print('Trimmed File Complete')


# BPM Counter
def HeartRate(filename):
    y, fs = librosa.load(filename)

    # Apply Adaptive Threasholding
    b, a = butter(3, 2 * 8 / fs, 'low')
    he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y)))))
    print('Adaptive Threasholding Complete')

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

    #Plot graph
    plt.plot(y)
    plt.plot(he, linewidth=2)
    plt.show()
    return BPM

filename = 'C:/Users/Matt/Documents/Project/CS-M/Datasets/normal/test/(1).wav'
trim_wav(filename,0,10)
BPM = HeartRate('File.wav')
print('BPM: ',BPM)