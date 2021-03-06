import os
import matplotlib.pyplot as plt
import numpy as np
#for loading and visualizing audio files
import librosa
import librosa.display
from scipy.io import wavfile

#to play audio
import IPython.display as ipd

def trim_wav( originalWavPath, newWavPath , start, end ):
    '''
    :param originalWavPath: the path to the source wav file
    :param newWavPath: output wav file * can be same path as original
    :param start: time in seconds
    :param end: time in seconds
    :return:
    '''
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( newWavPath, sampleRate, waveData[startSample:endSample])

path1 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest1.wav"
path2 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest2.wav"
path3 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest3.wav"
path4 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest4.wav"
path5 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest5.wav"
path6 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest6.wav"
path7 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest7.wav"
path8 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest8.wav"
path9 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Boya/BoyaTest9.wav"

Fpath1 = 'Sound1.wav'
Fpath2 = 'Sound2.wav'
Fpath3 = 'Sound3.wav'
Fpath4 = 'Sound4.wav'
Fpath5 = 'Sound5.wav'
Fpath6 = 'Sound6.wav'
Fpath7 = 'Sound7.wav'
Fpath8 = 'Sound8.wav'
Fpath9 = 'Sound9.wav'


trim_wav(path1,Fpath1,0,10)
trim_wav(path2,Fpath2,0,10)
trim_wav(path3,Fpath3,0,10)

x1, sr1 = librosa.load(Fpath1)
x2, sr2 = librosa.load(Fpath2)
x3, sr3 = librosa.load(Fpath3)
print(type(x1),type(sr1))

x = np.mean( np.array([ x1, x2,x3 ]), axis=0 )
sr = np.mean( np.array([sr1, sr2,sr3 ]), axis=0 )

print(type(x), type(sr))
print(x.shape, sr)

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
plt.show()
