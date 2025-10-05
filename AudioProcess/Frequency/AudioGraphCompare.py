import librosa
import matplotlib.pyplot as plt

# Load the audio file
filename1 = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Noisereduce/normal/(1-1).wav'
y1, sr1 = librosa.load(filename1)   

filename2 = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Noisereduce/normal/(2-1).wav'
y2, sr2 = librosa.load(filename2)

# Plot the filtered spectrum
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(y1)
plt.plot(y2)

plt.tight_layout()
plt.savefig('C:/Users/Matt/Downloads/(1).png')
plt.show()
