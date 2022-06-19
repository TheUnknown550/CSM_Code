# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import copy
from scipy.io import wavfile
from pydub import AudioSegment
from scipy.io.wavfile import write

#Variables
FilSig = []

#Value Use for creating wav file
samplerate = 44100  

#Sound Path
path = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test1.wav"

# shows the sound waves
raw = wave.open(path)
signal = raw.readframes(-1)
signal = np.frombuffer(signal, dtype ="int16")


# gets the frame rate
f_rate = raw.getframerate()
time = np.linspace(
    0, # start
    len(signal) / f_rate,
    num = len(signal)
)
CopSig = copy.deepcopy(signal)
signal = np.where((signal <= 1000)&(signal > -1000),0,signal)

        

#Create The New Wav File
write("C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile2.wav", samplerate, signal.astype(np.int16));print("Creating New WAV file is Done!")

#Graphing
plt.figure(1)
plt.title("Sound Wave")
plt.xlabel("Time")
plt.plot(time,CopSig)
plt.plot(time, signal)
plt.show()

