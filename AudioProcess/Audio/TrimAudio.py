from scipy.io import wavfile
import soundfile as sf
import matplotlib.pyplot as plt

file = 'C:/Users/Matt/Documents/Project/CS-M/Datasets/Datasets1/normal/test/(11).wav'
output = 'File.wav'
sampleRate, waveData = wavfile.read( file )
startSample = int( 1 * sampleRate )
endSample = int( 6 * sampleRate )
wavfile.write( output, sampleRate, waveData[startSample:endSample])

y, fs = sf.read(output)
plt.figure(figsize=(8, 4))
plt.plot(y)

plt.tight_layout()
plt.show()
