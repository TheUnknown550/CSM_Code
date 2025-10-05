import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.io import wavfile
import soundfile as sf
from scipy.signal import firwin, filtfilt

# Trim Audio
def trim_wav( originalWavPath, start, end, Name ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write(Name, sampleRate, waveData[startSample:endSample])

# Load the two audio files as NumPy arrays
File = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/normal/0dB/(1).wav'
trim_wav(File,0,10,'File.wav')
frames, sample_rate = sf.read('File.wav')

TestFile = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/Control/normal/(1).wav'
trim_wav(TestFile,0,10,'Test.wav')
Test, fs2 = sf.read('Test.wav')

# Band-pass Filter
# Define filter parameters
fmin = 20  # Lower cutoff frequency
fmax = 250  # Upper cutoff frequency

# Calculate the filter order
nyquist_freq = 0.5 * sample_rate
width = 100  # Width of the transition band, in Hz
n = int(np.ceil(4 * nyquist_freq / width))

# Design the bandpass filter
b = firwin(n, [fmin, fmax], pass_zero=False, fs=sample_rate)

# Apply the filter to the audio file
filtered_frames = filtfilt(b, [1], frames)



# Export new WAV file
sf.write('BandPass.wav', filtered_frames, sample_rate)


# Filter Effectiveness Tests
# Trim the ANC array to match the length of the Test array
filtered_frames = filtered_frames[:len(Test)]

signal_power = np.sum(Test**2)
noise_power = np.sum((filtered_frames)**2)
snr = 10 * np.log10(signal_power / noise_power)
print("SNR: {:.2f} dB".format(snr))
rmse = np.sqrt(np.mean((Test - filtered_frames)**2))
print("RMSE: {:.2f}".format(rmse))



'''# Plot sound graphs
t = np.arange(0, len(frames)/sample_rate, 1/sample_rate)
plt.figure(1)
plt.title("Sound Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.plot(t, frames)
plt.plot(t, filtered_frames)
plt.show()'''