# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
from pydub import AudioSegment
from scipy.io.wavfile import write

#Variables
FilSig = []

#Value Use for creating wav file
samplerate = 44100  

#Sound Path
path = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest1.wav"

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

#Create The New Wav File
write("C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile.wav", samplerate, FilSig.astype(np.int16));print("Creating New WAV file is Done!")

#Graphing
plt.figure(1)
plt.title("Sound Wave")
plt.xlabel("Time")
plt.plot(time, signal)
plt.plot(time, FilSig)
plt.show()

