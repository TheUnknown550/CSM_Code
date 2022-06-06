# imports
from math import fabs
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
from pydub import AudioSegment
 
def SortFunc(Sorting):
    Sorting.sort(reverse=True)
    return Sorting

def Graph(time,signal,EditSignal):
    plt.figure(1)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.plot(time, signal)
    #Changed Value Graph
    plt.plot(time, EditSignal)
    plt.show()

src = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Sounds/5inch1.mp3"
Filepath = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Sounds/TestingFile.wav"
# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(Filepath, format="wav")

#variables
RecSig = []
RecTime = []
ChangeSig = []
SortSig = []
counter = False

raw = wave.open(Filepath)
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
        counter = True

    if signal[i] <= 29000 and counter :
        SortSig = SortFunc(RecSig)
        HighSigIndex = RecSig.index(SortSig[0])

        #Check signal before highest
        

        counter = False

Graph(time,signal,ChangeSig)



