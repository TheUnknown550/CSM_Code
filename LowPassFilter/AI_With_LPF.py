from fileinput import filename
import numpy as np
import os
import math
import pandas as pd
import librosa
import librosa.display as display
import glob 
import matplotlib.pyplot as plt
import tensorflow
import contextlib
import openpyxl as px
import wave
from tensorflow.keras.models import load_model
from openpyxl.styles import PatternFill

mfccs = 0.0

def extract_data(file_name):
    # function to load files and extract features
    try:
        # here kaiser_fast is a technique used for faster extraction
        X, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        # we extract mfcc feature from data
        global mfccs
        mfccs = np.mean(librosa.feature.mfcc(
            y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
    except Exception as e:
        #Error Message
        print("Error encountered while parsing file: ")
    #Reshape data to be in the right matrix
    feature = np.array(mfccs).reshape([-1, 1])
    print(mfccs)
    return feature

# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
def running_mean(x, windowSize):
  cumsum = np.cumsum(np.insert(x, 0, 0)) 
  return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

# from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8 # unsigned char
    elif sample_width == 2:
        dtype = np.int16 # signed 2-byte short
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")

    channels = np.fromstring(raw_bytes, dtype=dtype)

    if interleaved:
        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
        channels.shape = (n_channels, n_frames)

    return channels

af = load_model('AI/Models/AF.h5')#AF AI Path
murmur = load_model('AI/Models/murmur.h5') #murmur AI Path
y = []
b = []
returnvalueAF1 = []
returnvalueAF2 = []
returnvalueAF3 = []
returnvalueAF4 = []
returnvalueAF5 = []
returnvalueAF6 = []

returnvalueMur1 = []
returnvalueMur2 = []
returnvalueMur3 = []
returnvalueMur4 = []
returnvalueMur5 = []
returnvalueMur6 = []

file = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22'#WAV File Path
#Make list for all files
file_name = [file+'/Test1.wav', file+'/Test2.wav', file+'/Test3.wav',
file+'/Test4.wav', file+'/Test5.wav', file+'/Test6.wav', file+'/Test7.wav',
file+'/Test8.wav', file+'/Test9.wav', file+'/Test10.wav', file+'/Test11.wav']

cutOffFrequency = [2.0,4.0,6.0,8.0,10.0]
outname1 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav'
outname2 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile2.wav'
outname3 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile3.wav'
outname4 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile4.wav'
outname5 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile5.wav'


def filtering(file):
    with contextlib.closing(wave.open(file,'rb')) as spf:
        sampleRate = spf.getframerate()
        ampWidth = spf.getsampwidth()
        nChannels = spf.getnchannels()
        nFrames = spf.getnframes()

        # Extract Raw Audio from multi-channel Wav File
        signal = spf.readframes(nFrames*nChannels)
        spf.close()
        channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

        # get window size
        # from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
        #50.0 cutoff
        freqRatio1 = (cutOffFrequency[0]/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio1**2)/freqRatio1)

        # Use moviung average (only on first channel)
        filtered = running_mean(channels[0], N).astype(channels.dtype)

        wav_file1 = wave.open(outname1, "w")
        wav_file1.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
        wav_file1.writeframes(filtered.tobytes('C'))
        wav_file1.close()


        #100.0 cutoff
        freqRatio2 = (cutOffFrequency[1]/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio2**2)/freqRatio2)

        # Use moviung average (only on first channel)
        filtered = running_mean(channels[0], N).astype(channels.dtype)

        wav_file2 = wave.open(outname2, "w")
        wav_file2.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
        wav_file2.writeframes(filtered.tobytes('C'))
        wav_file2.close()


        #200.0 cutoff
        freqRatio3 = (cutOffFrequency[2]/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio3**2)/freqRatio3)

        # Use moviung average (only on first channel)
        filtered = running_mean(channels[0], N).astype(channels.dtype)

        wav_file3 = wave.open(outname3, "w")
        wav_file3.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
        wav_file3.writeframes(filtered.tobytes('C'))
        wav_file3.close()


        #300.0 cutoff
        freqRatio4 = (cutOffFrequency[3]/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio4**2)/freqRatio4)

        # Use moviung average (only on first channel)
        filtered = running_mean(channels[0], N).astype(channels.dtype)

        wav_file4 = wave.open(outname4, "w")
        wav_file4.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
        wav_file4.writeframes(filtered.tobytes('C'))
        wav_file4.close()


        #400.o cutoff
        freqRatio5 = (cutOffFrequency[4]/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio5**2)/freqRatio5)

        # Use moviung average (only on first channel)
        filtered = running_mean(channels[0], N).astype(channels.dtype)

        wav_file5 = wave.open(outname5, "w")
        wav_file5.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
        wav_file5.writeframes(filtered.tobytes('C'))
        wav_file5.close()


for i in range (len(file_name)):
    filtering(file_name[i])
    data = extract_data(file_name[i])
    data1 = extract_data(outname1)
    data2 = extract_data(outname2)
    data3 = extract_data(outname3)
    data4 = extract_data(outname4)
    data5 = extract_data(outname5)

    #Analize Predict and Save the data
    af_result = af.predict(np.array(data))
    murmur_result = murmur.predict(np.array(data))
    y = af_result[0]
    b = murmur_result[0]

    af_result = af.predict(np.array(data1))
    murmur_result = murmur.predict(np.array(data1))
    y1 = af_result[0]
    b1 = murmur_result[0]

    af_result = af.predict(np.array(data2))
    murmur_result = murmur.predict(np.array(data2))
    y2 = af_result[0]
    b2 = murmur_result[0]

    af_result = af.predict(np.array(data3))
    murmur_result = murmur.predict(np.array(data3))
    y3 = af_result[0]
    b3 = murmur_result[0]

    af_result = af.predict(np.array(data4))
    murmur_result = murmur.predict(np.array(data4))
    y4 = af_result[0]
    b4 = murmur_result[0]

    af_result = af.predict(np.array(data5))
    murmur_result = murmur.predict(np.array(data5))
    y5 = af_result[0]
    b5 = murmur_result[0]

    #Make it in % instead of 0.
    af_return = y[0]*100
    murmur_return = b[0]*100

    #Show the ai confidence[AF,murmur]
    returnvalueAF1.append(af_return)
    returnvalueMur1.append(murmur_return)
    print('Normal: ',returnvalueAF1[i],' , ',returnvalueMur1[i])

    af_return = y1[0]*100
    murmur_return = b1[0]*100
    returnvalueAF2.append(af_return)
    returnvalueMur2.append(murmur_return)
    print(cutOffFrequency[0],' : ',returnvalueAF2[i],' , ',returnvalueMur2[i])

    af_return = y2[0]*100
    murmur_return = b2[0]*100
    returnvalueAF3.append(af_return)
    returnvalueMur3.append(murmur_return)
    print(cutOffFrequency[1],' : ',returnvalueAF3[i],' , ',returnvalueMur3[i])


    af_return = y3[0]*100
    murmur_return = b3[0]*100
    returnvalueAF4.append(af_return)
    returnvalueMur4.append(murmur_return)
    print(cutOffFrequency[2],' : ',returnvalueAF4[i],' , ',returnvalueMur4[i])

    af_return = y4[0]*100
    murmur_return = b4[0]*100
    returnvalueAF5.append(af_return)
    returnvalueMur5.append(murmur_return)
    print(cutOffFrequency[3],' : ',returnvalueAF5[i],' , ',returnvalueMur5[i])

    af_return = y5[0]*100
    murmur_return = b5[0]*100
    returnvalueAF6.append(af_return)
    returnvalueMur6.append(murmur_return)
    print(cutOffFrequency[4],' : ',returnvalueAF6[i],' , ',returnvalueMur6[i])

