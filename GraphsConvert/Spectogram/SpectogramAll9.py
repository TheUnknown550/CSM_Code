import os
from tkinter.filedialog import SaveFileDialog
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

path1 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest1.wav"
path2 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest2.wav"
path3 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest3.wav"
path4 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest4.wav"
path5 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest5.wav"
path6 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest6.wav"
path7 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest7.wav"
path8 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest8.wav"
path9 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/Contact/ConTest9.wav"
SaveFile = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/Contact/ContactSpectrogramAll.png'

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
trim_wav(path4,Fpath4,0,10)
trim_wav(path5,Fpath5,0,10)
trim_wav(path6,Fpath6,0,10)
trim_wav(path7,Fpath7,0,10)
trim_wav(path8,Fpath8,0,10)
trim_wav(path9,Fpath9,0,10)

x1, sr1 = librosa.load(Fpath1)
x2, sr2 = librosa.load(Fpath2)
x3, sr3 = librosa.load(Fpath3)
x4, sr4 = librosa.load(Fpath4)
x5, sr5 = librosa.load(Fpath5)
x6, sr6 = librosa.load(Fpath6)
x7, sr7 = librosa.load(Fpath7)
x8, sr8 = librosa.load(Fpath8)
x9, sr9 = librosa.load(Fpath9)

x = np.mean( np.array([ x1, x2,x3,x4, x5,x6,x7, x8,x9 ]), axis=0 )
sr = np.mean( np.array([sr1, sr2,sr3,sr4, sr5,sr6,sr7, sr8,sr9 ]), axis=0 )


X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
fig, ax = plt.subplots()
D_highres = librosa.stft(x, hop_length=100, n_fft=500)
S_db_hr = librosa.amplitude_to_db(np.abs(D_highres), ref=np.max, amin=1e-05, top_db=90)
img = librosa.display.specshow(S_db_hr, hop_length=100, x_axis='time', y_axis='linear',ax=ax)
fig.colorbar(img, ax=ax, format="%+2.f dB")
#plt.show()
plt.savefig(SaveFile)

