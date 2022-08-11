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

path1 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Redmi Bud 3 lite/BudTest1.wav"
path2 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Redmi Bud 3 lite/BudTest2.wav"
path3 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Redmi Bud 3 lite/BudTest3.wav"

Fpath1 = 'Sound1.wav'
Fpath2 = 'Sound2.wav'
Fpath3 = 'Sound3.wav'

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
fig, ax = plt.subplots()
D_highres = librosa.stft(x, hop_length=100, n_fft=500)
S_db_hr = librosa.amplitude_to_db(np.abs(D_highres), ref=np.max, amin=1e-05, top_db=90)
img = librosa.display.specshow(S_db_hr, hop_length=100, x_axis='time', y_axis='linear',ax=ax)
fig.colorbar(img, ax=ax, format="%+2.f dB")
plt.show()

