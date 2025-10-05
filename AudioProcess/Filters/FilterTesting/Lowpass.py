import numpy as np
import scipy.signal as signal
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
import soundfile as sf

# Trim Audio
def trim_wav( originalWavPath, start, end, Name ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write(Name, sampleRate, waveData[startSample:endSample])

# Load the two audio files as NumPy arrays
File = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/Control/normal/(1).wav'
trim_wav(File,0,10,'File.wav')
frames, sample_rate = sf.read('File.wav')

TestFile = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/Control/normal/(1).wav'
trim_wav(TestFile,0,10,'Test.wav')
Test, fs2 = sf.read('Test.wav')

# Convert the frames to a numpy array
#frames = np.frombuffer(frames, dtype=np.int16)

# Low-pass filter
cutoff_freq = 200 # set cutoff frequency
nyq_freq = 0.5 * sample_rate # Nyquist frequency
Wn = cutoff_freq / nyq_freq # filter cutoff frequency
b, a = signal.cheby1(4, 5, Wn, btype='low', analog=False)
filtered_frames = signal.filtfilt(b, a, frames)


# Export new WAV file
sf.write('File.wav', filtered_frames, sample_rate)


# Filter Effectiveness Tests
# Calculate the SNR and RMSE values
signal_power = np.sum(Test**2)
noise_power = np.sum((filtered_frames)**2)
snr = 10 * np.log10(signal_power / noise_power)
print("SNR: {:.2f} dB".format(snr))
rmse = np.sqrt(np.mean((Test - filtered_frames)**2))
print("RMSE: {:.2f}".format(rmse))


# Plot sound graphs
t = np.arange(0, len(frames)/sample_rate, 1/sample_rate)
plt.figure(1)
plt.title("Sound Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.plot(t, frames)
plt.plot(t, filtered_frames)
plt.show()