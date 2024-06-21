from scipy.io import wavfile
import time

start_time = time.time()
sr, y = wavfile.read('C:/Users/matt_c/Documents/Projects/CS-M/Datasets/10Sec/AF/(1).wav')
scipy_duration = time.time() - start_time
print(scipy_duration)