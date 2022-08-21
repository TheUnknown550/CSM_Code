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

name = 'Bud'

path1 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest1.wav"
path2 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest2.wav"
path3 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest3.wav"
path4 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest4.wav"
path5 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest5.wav"
path6 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest6.wav"
path7 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest7.wav"
path8 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest8.wav"
path9 = "C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Sounds/"+name+"/BudTest9.wav"
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


X1 = librosa.stft(x1)
Xdb1 = librosa.amplitude_to_db(abs(X1))
fig1, ax1 = plt.subplots()
D_highres1 = librosa.stft(x1, hop_length=100, n_fft=500)
S_db_hr1 = librosa.amplitude_to_db(np.abs(D_highres1), ref=np.max, amin=1e-05, top_db=90)
img1 = librosa.display.specshow(S_db_hr1, hop_length=100, x_axis='time', y_axis='linear',ax=ax1)
fig1.colorbar(img1, ax=ax1, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram1.png')

X2 = librosa.stft(x2)
Xdb2 = librosa.amplitude_to_db(abs(X2))
fig2, ax2 = plt.subplots()
D_highres2 = librosa.stft(x2, hop_length=100, n_fft=500)
S_db_hr2 = librosa.amplitude_to_db(np.abs(D_highres2), ref=np.max, amin=1e-05, top_db=90)
img2 = librosa.display.specshow(S_db_hr2, hop_length=100, x_axis='time', y_axis='linear',ax=ax2)
fig2.colorbar(img2, ax=ax2, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram2.png')

X3 = librosa.stft(x3)
Xdb3 = librosa.amplitude_to_db(abs(X3))
fig3, ax3 = plt.subplots()
D_highres3 = librosa.stft(x3, hop_length=100, n_fft=500)
S_db_hr3 = librosa.amplitude_to_db(np.abs(D_highres3), ref=np.max, amin=1e-05, top_db=90)
img3 = librosa.display.specshow(S_db_hr3, hop_length=100, x_axis='time', y_axis='linear',ax=ax3)
fig3.colorbar(img3, ax=ax3, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram3.png')

X4 = librosa.stft(x4)
Xdb4 = librosa.amplitude_to_db(abs(X4))
fig4, ax4 = plt.subplots()
D_highres4 = librosa.stft(x4, hop_length=100, n_fft=500)
S_db_hr4 = librosa.amplitude_to_db(np.abs(D_highres4), ref=np.max, amin=1e-05, top_db=90)
img4 = librosa.display.specshow(S_db_hr4, hop_length=100, x_axis='time', y_axis='linear',ax=ax4)
fig4.colorbar(img4, ax=ax4, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram4.png')

X5 = librosa.stft(x5)
Xdb5 = librosa.amplitude_to_db(abs(X5))
fig5, ax5 = plt.subplots()
D_highres5 = librosa.stft(x5, hop_length=100, n_fft=500)
S_db_hr5 = librosa.amplitude_to_db(np.abs(D_highres5), ref=np.max, amin=1e-05, top_db=90)
img5 = librosa.display.specshow(S_db_hr5, hop_length=100, x_axis='time', y_axis='linear',ax=ax5)
fig5.colorbar(img5, ax=ax5, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram5.png')

X6 = librosa.stft(x6)
Xdb6 = librosa.amplitude_to_db(abs(X6))
fig6, ax6 = plt.subplots()
D_highres6 = librosa.stft(x6, hop_length=100, n_fft=500)
S_db_hr6 = librosa.amplitude_to_db(np.abs(D_highres6), ref=np.max, amin=1e-05, top_db=90)
img6 = librosa.display.specshow(S_db_hr6, hop_length=100, x_axis='time', y_axis='linear',ax=ax6)
fig6.colorbar(img6, ax=ax6, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram6.png')

X7 = librosa.stft(x7)
Xdb7 = librosa.amplitude_to_db(abs(X7))
fig7, ax7 = plt.subplots()
D_highres7 = librosa.stft(x7, hop_length=100, n_fft=500)
S_db_hr7 = librosa.amplitude_to_db(np.abs(D_highres7), ref=np.max, amin=1e-05, top_db=90)
img7 = librosa.display.specshow(S_db_hr7, hop_length=100, x_axis='time', y_axis='linear',ax=ax7)
fig7.colorbar(img7, ax=ax7, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram7.png')

X8 = librosa.stft(x8)
Xdb8 = librosa.amplitude_to_db(abs(X8))
fig8, ax8 = plt.subplots()
D_highres8 = librosa.stft(x8, hop_length=100, n_fft=500)
S_db_hr8 = librosa.amplitude_to_db(np.abs(D_highres8), ref=np.max, amin=1e-05, top_db=90)
img8 = librosa.display.specshow(S_db_hr8, hop_length=100, x_axis='time', y_axis='linear',ax=ax8)
fig8.colorbar(img8, ax=ax8, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram8.png')

X9 = librosa.stft(x9)
Xdb9 = librosa.amplitude_to_db(abs(X9))
fig9, ax9 = plt.subplots()
D_highres9 = librosa.stft(x9, hop_length=100, n_fft=500)
S_db_hr9 = librosa.amplitude_to_db(np.abs(D_highres9), ref=np.max, amin=1e-05, top_db=90)
img9 = librosa.display.specshow(S_db_hr9, hop_length=100, x_axis='time', y_axis='linear',ax=ax9)
fig9.colorbar(img9, ax=ax9, format="%+2.f dB")
plt.savefig('C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/MicType/Spectrogram/'+name+'/'+name+'Spectrogram9.png')

