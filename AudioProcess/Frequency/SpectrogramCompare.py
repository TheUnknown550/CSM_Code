import librosa
import matplotlib.pyplot as plt

# Load the audio file
filename1 = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Noisereduce/normal/(1-1).wav'
filename2 = "C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Heart/normal/(1).wav"
y1, sr1 = librosa.load(filename1)
y2, sr2 = librosa.load(filename2)

# Compute the Fourier transform of the audio signal
fft1 = librosa.stft(y1)
fft2 = librosa.stft(y2)

# Convert the complex Fourier coefficients to magnitudes
mag2 = librosa.amplitude_to_db(abs(fft2))
mag1 = librosa.amplitude_to_db(abs(fft1))

# Plot the filtered spectrum
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
librosa.display.specshow(mag1, sr=sr1, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Filtered Spectrogram')

# Plot the based spectrum
plt.subplot(2, 1, 2)
librosa.display.specshow(mag2, sr=sr2, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Based Spectrogram')

plt.tight_layout()
plt.show()
