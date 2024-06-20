# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.signal import find_peaks
 
# shows the sound waves
def visualize(path: str):
    raw = wave.open(path)

    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
    
    
    
    # gets the frame rate
    f_rate = raw.getframerate()

    time = np.linspace(
        0, # start
        len(signal) / f_rate,
        num = len(signal)
    )

    Avgsig = np.average(np.abs(signal))
    peaks, _ = find_peaks(signal, height = Avgsig*5)
    print(Avgsig*5)
    Avg = np.average(signal[peaks])
    print(Avg)

    plt.figure(1)

    plt.title("Sound Wave")

    plt.xlabel("Time")

    plt.plot(time, signal)

    #plt.show()


if __name__ == "__main__":

    Filepath = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest1.wav"
 
    visualize(Filepath)