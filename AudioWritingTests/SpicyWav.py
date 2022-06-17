import numpy as np
from scipy.io.wavfile import write

samplerate = 44100  
freq = 100
seconds = 5
time = np.linspace(0., seconds, seconds*samplerate, endpoint=False)
signal = np.sin(2*np.pi*freq*time)

# The final amplitude should span the signed 16-bit integers range [-2**15,2**15)
amplitude = np.iinfo(np.int16).max # iinfo returns the range for the int16 type, then max resolves to -> 2**15 
data = amplitude * signal 
write("C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile.wav", samplerate, data.astype(np.int16))