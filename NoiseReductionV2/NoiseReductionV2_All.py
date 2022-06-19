import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks
import wave
import sys
import contextlib
import copy
from scipy.io.wavfile import write

#Value Use for creating wav file
samplerate = 44100  


audioname = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A51/Test11.wav'
outFile = ['C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav',
'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile2.wav',
'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile3.wav',
'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile4.wav',
'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile5.wav']
spf = wave.open(audioname)
# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.frombuffer(signal, "int16")
fs = spf.getframerate()
Time = np.linspace(0, len(signal) / fs, num=len(signal))

#step2
ab_signal = np.abs(signal)
#step3
signal_filtered = savgol_filter(ab_signal, 4999, 3)
#step4
peaks2, _ = find_peaks(signal_filtered, prominence=250) 
peaks2.sort()
maxSigP =  signal_filtered[peaks2[0]]
maxSigN = -abs(signal_filtered[peaks2[0]])

CopSig = copy.deepcopy(signal)
signals = [np.where((signal <= maxSigP)&(signal > maxSigN),signal/2,signal),
np.where((signal <= maxSigP)&(signal > maxSigN),signal*2/3,signal),
np.where((signal <= maxSigP)&(signal > maxSigN),signal*3/4,signal),
np.where((signal <= maxSigP)&(signal > maxSigN),signal*4/5,signal),
np.where((signal <= maxSigP)&(signal > maxSigN),signal*5/6,signal)]


#Create The New Wav File
write(outFile[0], samplerate, signals[0].astype(np.int16));print("Creating New WAV_1 file is Done!")
write(outFile[1], samplerate, signals[1].astype(np.int16));print("Creating New WAV_2 file is Done!")
write(outFile[2], samplerate, signals[2].astype(np.int16));print("Creating New WAV_3 file is Done!")
write(outFile[3], samplerate, signals[3].astype(np.int16));print("Creating New WAV_4 file is Done!")
write(outFile[4], samplerate, signals[4].astype(np.int16));print("Creating New WAV_5 file is Done!")

#Graphing
plt.figure(1)
plt.title("Sound Wave")
plt.xlabel("Time")
plt.plot(Time,CopSig)
plt.plot(Time, signal)
#plt.show()
