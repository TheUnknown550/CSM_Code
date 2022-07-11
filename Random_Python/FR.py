#A short example to extract the frequency spectrum of a signal
import numpy as np
import matplotlib.pyplot as plt
import wave

path = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav'
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

fourierTransform = np.fft.fft(signal)/len(signal)
fourierTransform = fourierTransform[range(int(len(signal)/2))]
tpCount     = len(signal)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/f_rate
frequencies = values/timePeriod
plt.plot(frequencies, abs(fourierTransform))
plt.show()