import os
import matplotlib.pyplot as plt
import numpy as np
#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

path = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Contact/ConTest9.wav"

x, sr = librosa.load(path)

print(type(x), type(sr))
print(x.shape, sr)

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
plt.show()
