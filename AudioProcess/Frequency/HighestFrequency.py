import numpy as np
import soundfile as sf
from scipy.signal import stft
from scipy.io import wavfile

# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])
    print('Trimmed File Complete')

# Load the audio file
File = 'C:/Users/Matt/Documents/Project/CS-M/Datasets/normal/test/(1).wav'
trim_wav(File,0,10)
signal, fs = sf.read('File.wav')

# Define the window size and overlap
window_size = int(0.01 * fs) # 10 ms
overlap = int(0.5 * window_size) # 50% overlap

# Apply STFT to the signal
f, t, Zxx = stft(signal, fs=fs, window='hann', nperseg=window_size, noverlap=overlap)

# Get the magnitude and phase of the STFT
magnitude = np.abs(Zxx)
phase = np.angle(Zxx)

# Get the dominant frequency in each time frame
dominant_freq = np.argmax(magnitude, axis=0)

# Print the dominant frequency in each time frame
for i in range(len(t)):
    print("Time frame {}: Dominant frequency = {:.2f} Hz".format(i+1, f[dominant_freq[i]]))
