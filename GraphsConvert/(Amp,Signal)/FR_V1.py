# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import librosa
from scipy.io import wavfile
from os import path
from pydub import AudioSegment


audio = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test7.wav'

raw = wave.open(audio)
signal = raw.readframes(-1)
signal = np.frombuffer(signal, dtype ="int16")
db = librosa.amplitude_to_db(abs(signal))

plt.plot(abs(signal))
plt.show()