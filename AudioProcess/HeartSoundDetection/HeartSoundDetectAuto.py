# Imports
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter,hilbert, filtfilt,correlate, find_peaks
from scipy.io import wavfile

# Variables
S1 = []
S2 = []

# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])
    print('Trimmed File Complete')

# Automation
for i in range(344,1000):
    print(i+1)
    #Load Audio
    filename = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/AmpLowTests/murmur/AmpToLow/LowAudio2/('+str(i+1)+').wav'
    #trim_wav(filename,0,10)
    
    # BPM Counter
    # Load audio
    y, fs = librosa.load(filename)
    
    # Apply Adaptive Threasholding
    b, a = butter(4, 2 * 8 / fs, 'low')
    he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y)))))
    print('Adaptive Threasholding Complete')
    
    # Calculate BPM
    x = he - np.mean(he)
    corr = correlate(x, x, mode='same')  
    corr = corr[int(corr.size/2):]
    min_index = int(0.5*fs)
    max_index = int(2*fs)
    index = np.argmax(corr[min_index:max_index])
    true_index = index+min_index
    BPM = 60/(true_index/fs)
    print('BPM Calculate Complete')
    print('BPM: ',BPM)
    
    # Find peaks
    height = np.mean(he)
    
    peaks, _ = find_peaks(he, height=height)
    
    # Find S1 and S2 of sound
    for n in range(len(peaks)):
        if (n+3) <= len(peaks):
            
            # Finding space between each beat
            space1 = he[peaks[n+1]] - he[peaks[n]]
            space2 = he[peaks[n+2]] - he[peaks[n+1]]
    
            # Detecting S1/S2
            if space1 >= space2:
                S2.append(peaks[n])
            else:
                S1.append(peaks[n])
        elif (n+2)<=len(peaks):
            if peaks[n-1] == S2[len(S2)-1]:
                S1.append(peaks[n])
                S2.append(peaks[n+1])
            elif peaks[n-1] == S1[len(S1)-1]:
                S2.append(peaks[n])
                S1.append(peaks[n+1])
            
    
    
    #Plot graph
    plt.title('Sound Graph')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    bbox_props = dict(boxstyle="round", fc="white", ec="black", lw=0.5, alpha=0.5)
    plt.text(0.95, 0.95, f'BPM: {BPM:.2f}', transform=plt.gca().transAxes,
             fontsize=14, verticalalignment='top', horizontalalignment='right',
             bbox=bbox_props)
    plt.plot(y, label='Sound')
    plt.plot(he, linewidth=2, label='Adaptive Threasholding')
    plt.plot(S1, he[S1],'ro', label='S1', color='g')
    plt.plot(S2, he[S2],'ro', label='S2', color='r')
    
    plt.legend()
    #plt.show()
    S1.clear()
    S2.clear()
    plt.savefig('C:/Users/Matt/Documents/Project/CS-M/Experiments/AmpLowTests/murmur/AmpToLow/S1S2/('+str(i+1)+').png')
    plt.clf()
    