import librosa
import time

start_time = time.time()
y, sr = librosa.load('C:/Users/matt_c/Documents/Projects/CS-M/Datasets/10Sec/AF/(1).wav', sr=None)
librosa_duration = time.time() - start_time
print(librosa_duration)
