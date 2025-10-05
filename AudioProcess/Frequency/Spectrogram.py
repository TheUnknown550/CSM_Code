import librosa
import matplotlib.pyplot as plt
from scipy.io import wavfile


y, sr = librosa.load("C:/Users/Matt/Documents/Project/CS-M/Datasets/Datasets1/normal/test/(6).wav")

# Compute the Fourier transform of the audio signal
fft = librosa.stft(y)

# Convert the complex Fourier coefficients to magnitudes 
mag = librosa.amplitude_to_db(abs(fft))

# Plot the filtered spectrum
plt.figure(figsize=(8, 4))
#plt.subplot(2, 1, 1)
#librosa.display.specshow(mag, sr=sr, x_axis='time', y_axis='log')
#plt.colorbar(format='%+2.0f dB')
#plt.title('Spectrogram')

#plt.subplot(2, 1, 2)
plt.plot(y)

plt.tight_layout()
plt.show()
