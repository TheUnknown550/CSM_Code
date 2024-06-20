from scipy.io import wavfile
import noisereduce as nr
# load data
rate, data = wavfile.read("C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test7.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write("C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav", rate, reduced_noise)