import numpy as np
import scipy.signal as signal
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
import soundfile as sf

# Trim the Audio
def trim_wav( originalWavPath, start, end, name ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( name, sampleRate, waveData[startSample:endSample])


# Automatin
for i in range(1000):
    print(i+1)
    # Load audio file
    # Trim and Load the audio file
    trim_wav("C:/Users/Matt/Documents/Project/CS-M/Datasets/Datasets/Normal/("+str(i+1)+").wav", 0,10, 'File.wav')

    frames, sample_rate = sf.read('File.wav')

    # Convert the frames to a numpy array
    #frames = np.frombuffer(frames, dtype=np.int16)

    # Low-pass filter
    cutoff_freq = 200 # set cutoff frequency
    nyq_freq = 0.5 * sample_rate # Nyquist frequency
    Wn = cutoff_freq / nyq_freq # filter cutoff frequency
    b, a = signal.cheby1(4, 5, Wn, btype='low', analog=False)
    filtered_frames = signal.filtfilt(b, a, frames)


    # Export new WAV file
    sf.write('C:/Users/Matt/Documents/Project/CS-M/Experiments/AmpLowTests/Normal/LowToAmp/LowAudio1/('+str(i+1)+').wav', filtered_frames, sample_rate)
