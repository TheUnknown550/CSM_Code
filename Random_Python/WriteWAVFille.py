# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
#from pydub import AudioSegment
from scipy.io.wavfile import write

#Variables
FilSig = []

#Value Use for creating wav file
samplerate = 44100  

#Sound Path
path = "C:/Users/matt_c/Documents/Projects/CS-M/Datasets/10Sec/AF/(10).wav"

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

#Graphing
plt.figure(1)
plt.title("Sound Wave")
plt.xlabel("Time")
plt.plot(time, signal)
plt.show()

