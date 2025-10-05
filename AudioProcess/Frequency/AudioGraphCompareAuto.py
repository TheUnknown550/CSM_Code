import numpy as np
import soundfile as sf
from scipy.io import wavfile

# Trim Audio
def trim_wav( originalWavPath, start, end, Name ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write(Name, sampleRate, waveData[startSample:endSample])

# Load the two audio files as NumPy arrays
File = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/normal/20dB/(1).wav'
trim_wav(File,0,10,'File.wav')
Original, fs1 = sf.read('File.wav')

NoiseFile = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/Noises/20dB.wav'
trim_wav(NoiseFile,0,10,'Noise.wav')
Noise, fs2 = sf.read('Noise.wav')

TestFile = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/Control/normal/(1).wav'
trim_wav(TestFile,0,10,'Test.wav')
Test, fs3 = sf.read('Test.wav')

# Flatten the arrays
Original = Original.ravel()
Noise = Noise.ravel()
Test= Test.ravel()

# Ensure that the two audio files have the same length
min_len = min(len(Original), len(Noise))
Original = Original[:min_len]
Noise = Noise[:min_len]

# Define a filter function that generates the filter coefficients
def create_filter(signal, noise):
    corr = np.correlate(signal, noise, mode='full')
    delay = np.argmax(corr)
    start = max(0, delay - len(noise) + 1)
    end = min(len(signal), delay + 1)
    signal_reg = signal + 1e-10  # Add a small positive value to signal to avoid divide-by-zero
    filter_coef = np.zeros_like(signal)
    filter_coef[start:end] = noise[:end-start] / signal_reg[start:end]
    return filter_coef

# Generate the noise filter coefficients using the two audio files
filter_coef = create_filter(Original, Noise)

# Create an array of zeros with the same length as the noise file
Silence = np.zeros_like(Noise)

# Apply the noise filter to the array of zeros to create a new "silenced" noise array
SilencedNoise = np.convolve(Silence, filter_coef, mode='same')

# Add the silenced noise array to the original audio to replace the noise with silence
Silenced = Original + SilencedNoise

# Save the filtered audio to a new file
sf.write('ANC.wav', Silenced, fs1)

# Trim the Silenced array to match the length of the Test array
Silenced = Silenced[:len(Test)]

# Calculate the SNR and RMSE values
signal_power = np.sum(Test**2) / len(Test)
noise_power = np.sum((SilencedNoise)**2) / len(SilencedNoise)
snr = 10 * np.log10(signal_power / noise_power)
print("SNR: {:.2f} dB".format(snr))
rmse = np.sqrt(np.mean((Test - Silenced)**2))

# Print the SNR and RMSE values to the console
print("RMSE: {:.4f}".format(rmse))
