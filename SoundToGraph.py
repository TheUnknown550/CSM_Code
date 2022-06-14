# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
from pydub import AudioSegment
 
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

    plt.figure(1)

    plt.title("Sound Wave")

    plt.xlabel("Time")

    plt.plot(time, signal)

    plt.show()


if __name__ == "__main__":

    src = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/SpongeTest/A51/Test1.wav"
    Filepath = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/TestingFile.wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(Filepath, format="wav")
 
    visualize(Filepath)