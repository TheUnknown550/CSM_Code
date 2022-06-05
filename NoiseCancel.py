# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
 
# shows the sound waves
def visualize(path: str):
    RecTime = []
    RecSig = []
    CheckSigHigh= []
    CheckTimeHigh= []
    CheckTimeLow= []
    CheckSigLow= []
    counter = 0
    counters = 0
    TimeHighPoint = 0
    SumTimeHighPoint = 0
    TimeHighMax = 0
    TimeHighMin = 0

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
    #Note!! play with signal instead of time
    for i in range(len(signal)):
        
        if signal [i] > 2750:
            CheckSigHigh.append(signal[i])
            CheckTimeHigh.append(round(time[i],3))
            if counter == 0:
                counter = 1
            
        
        if signal[i] < 2750 and counter == 1:
            #Way 1 use Time Avg per each graph
            for n in range (len(CheckTimeHigh)):
                SumTimeHighPoint = SumTimeHighPoint + CheckTimeHigh[n]
            TimeHighPoint = SumTimeHighPoint/int(len(CheckTimeHigh))
            SumTimeHighPoint = 0

            #Find Highest Point of signal
            CheckSigHigh.sort(reverse=True)

            #Add the highest variables to list
            RecTime.append(TimeHighPoint)
            RecSig.append(CheckSigHigh[0])

            #Resets variables for later use
            TimeHighPoint = 0
            counter = 0
            
            #Clear list for later use
            CheckSigHigh.clear()
            CheckTimeHigh.clear()



        if signal [i] < -2600:
            CheckSigLow.append(signal[i])
            CheckTimeLow.append(round(time[i],3))
            if counter == 0:
                counter = 1

        if signal[i] > -2600 and counter == 1:
            for m in range (len(CheckTimeLow)):
                SumTimeLowPoint = SumTimeLowPoint + CheckTimeLow[m]
            TimeLowPoint = SumTimeLowPoint/int(len(CheckTimeLow))
            SumTimeLowPoint = 0

            #Find Highest Point of signal
            CheckSigLow.sort(reverse=True)

            #Add the highest variables to list
            RecTime.append(TimeLowPoint)
            RecSig.append(CheckSigLow[0])

            #Resets variables for later use
            TimeLowPoint = 0
            counter = 0
            
            #Clear list for later use
            CheckSigLow.clear()
            CheckTimeLow.clear()

        if signal[i] == 0:
            RecTime.append(round(time[i],3))
            RecSig.append(signal[i])

    '''print(RecTime)
    print(len(RecTime))
    print(RecSig)
    print(len(RecSig))'''

    plt.figure(1)

    plt.title("Sound Wave")

    plt.xlabel("Time")

    plt.plot(time, signal)
    plt.plot(RecTime, RecSig)

    plt.show()


if __name__ == "__main__":

    path = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Sounds/.wav'
 
    visualize(path)