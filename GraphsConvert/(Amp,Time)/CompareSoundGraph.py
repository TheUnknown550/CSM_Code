# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
from os import path
from pydub import AudioSegment


# shows the sound waves
def visualize(Filepath: str, FilteredPath: str):
    # reading the audio file
    raw = wave.open(Filepath)
    FilteredRaw = wave.open(FilteredPath)
     
    # reads all the frames
    # -1 indicates all or max frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")

    FilteredSig = FilteredRaw.readframes(-1)
    FilteredSig = np.frombuffer(FilteredSig, dtype ="int16")
    
    
    
    # gets the frame rate
    f_rate = raw.getframerate()
    FilterRate = FilteredRaw.getframerate()
 
    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    time = np.linspace(
        0, # start
        len(signal) / f_rate,
        num = len(signal)
    )

    FilteredTime = np.linspace(
        0,
        len(FilteredSig) / FilterRate,
        num = len(FilteredSig)
    )

    # using matplotlib to plot
    # creates a new figure
    plt.figure(1)
     
    # title of the plot
    plt.title("Sound Wave")
     
    # label of x-axis
    plt.xlabel("Time")
    
    # actual plotting
    plt.plot(time, signal, label='File1')
    plt.plot(FilteredTime, FilteredSig, linewidth = 2,label='File2')
    plt.legend()
    # shows the plot
    # in new window
    plt.show()

 

if __name__ == "__main__":

    # files                                                                         
    Filepath = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test7.wav"

    # gets the command line Value'''
    FilePath1 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav'
 
    visualize(Filepath,FilePath1)