import os
import matplotlib.pyplot as plt
import numpy as np
#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

path = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Contact/ConTest6.wav"

x, sr = librosa.load(path)

print(type(x), type(sr))
print(x.shape, sr)

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
fig, ax = plt.subplots()
D_highres = librosa.stft(x, hop_length=100, n_fft=500)
S_db_hr = librosa.amplitude_to_db(np.abs(D_highres), ref=np.max, amin=1e-05, top_db=90)
img = librosa.display.specshow(S_db_hr, hop_length=100, x_axis='time', y_axis='linear',ax=ax)
fig.colorbar(img, ax=ax, format="%+2.f dB")
plt.show()

