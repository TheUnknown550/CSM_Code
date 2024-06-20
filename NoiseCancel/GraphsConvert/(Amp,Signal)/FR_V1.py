# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys



audio = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test7.wav'

raw = wave.open(audio)
signal = raw.readframes(-1)
signal = np.frombuffer(signal, dtype ="int16")
spectrum = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(spectrum))
plt.plot(frequencies,spectrum)
plt.show()