# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
from os import path
from pydub import AudioSegment
from scipy.signal import find_peaks


def Graphing(File, int, name):
    # reading the audio file
    raw = wave.open(File)

    # reads all the frames
    # -1 indicates all or max frames
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
    peaks, _ = find_peaks(signal, height = Avgsig*8)
    Avg = np.average(signal[peaks])
    print(int,":",Avg)

    # title of the plot
    plt.title("Sound Wave")
    
    # label of x-axis
    plt.xlabel("Time")

    # actual plotting
    plt.plot(time, signal)
    #plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/AmpTimeGraph/'+name+'/'+name+'AmpTimeGraph'+int+'.png')
    plt.close()

    return Avg

 
# Varibles
name = 'Contact'                                                                         
File1 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest1.wav'
File2 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest2.wav'
File3 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest3.wav'
File4 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest4.wav'
File5 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest5.wav'
File6 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest6.wav'
File7 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest7.wav'
File8 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest8.wav'
File9 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/'+name+'/ConTest9.wav'

Avg = []

Avg.append(Graphing(File1,'1',name))
Avg.append(Graphing(File2,'2',name))
Avg.append(Graphing(File3,'3',name))
Avg.append(Graphing(File4,'4',name))
Avg.append(Graphing(File5,'5',name))
Avg.append(Graphing(File6,'6',name))
Avg.append(Graphing(File7,'7',name))
Avg.append(Graphing(File8,'8',name))
Avg.append(Graphing(File9,'9',name))

TotalAvg = np.average(Avg)
print(TotalAvg)

