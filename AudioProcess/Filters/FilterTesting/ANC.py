import numpy as np
import soundfile as sf
from scipy.io import wavfile
import noisereduce as nr

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
Test = Test[:min_len]

ANC = nr.reduce_noise(y=Original, y_noise=Noise, sr=fs1, time_mask_smooth_ms= 128, prop_decrease=0.)


# Save the filtered audio to a new file
sf.write('ANC.wav', ANC, fs1)

# Trim the ANC array to match the length of the Test array
ANC = ANC[:len(Test)]

# Calculate the SNR and RMSE values
signal_power = np.sum(Test**2)
noise_power = np.sum((ANC)**2)
snr = 10 * np.log10(signal_power / noise_power)
print("SNR: {:.2f} dB".format(snr))
rmse = np.sqrt(np.mean((Test - ANC)**2))
print("RMSE: {:.2f}".format(rmse))


