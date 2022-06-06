# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
from pydub import AudioSegment
 

# shows the sound waves
def visualize(path: str):

    #variables
    RecSig = []
    RecTime = []
    ChangeSig = []

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

    #Check each value in graph
    for i in range (len(time)):
        #Record Value in graph
        ChangeSig.append(signal[i])
        if signal[i] > 29000:
            #change Value of recorded graph
            ChangeSig[i] = 0
            #Record the changed value
            RecSig.append(signal[i])
            RecTime.append(round(time[i],3))

            SortSig = RecSig.sort(reverse=True)
            print(RecSig)


    plt.figure(1)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.plot(time, signal)

    #Changed Value Graph
    plt.plot(time, ChangeSig)
    plt.show()


if __name__ == "__main__":

    src = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Sounds/5inch1.mp3"
    Filepath = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Sounds/TestingFile.wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(Filepath, format="wav")
 
    visualize(Filepath)