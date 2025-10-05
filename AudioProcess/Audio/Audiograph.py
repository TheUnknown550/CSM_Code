import librosa
import matplotlib.pyplot as plt

# Load the audio file
filename1 = 'C:/Users/Matt/Documents/Project/CS-M/Datasets/Datasets/Normal/(2).wav'
y1, sr1 = librosa.load(filename1)

# Plot the filtered spectrum
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(y1)
plt.tight_layout()
plt.show()
