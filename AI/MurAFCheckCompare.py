import numpy as np
import os
import pandas as pd
import librosa
import librosa.display as display
import glob 
import matplotlib.pyplot as plt
import tensorflow
from tensorflow.keras.models import load_model


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

af = load_model('AI/Models/AF.h5')#AF AI Path
murmur = load_model('AI/Models/murmur.h5') #murmur AI Path

#variables
mfccs = 0.0
data1 = []
data2 = []
result = []
file_name1 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A51/Test5.wav' #WAV File Path
file_name2 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav'

#Extract and read the WAV file for the AI
a1 = extract_data(file_name1)
data1.append(a1)

a2 = extract_data(file_name2)
data2.append(a2)

#Analize Predict and Save the data
af_result = af.predict(np.array(data1))
murmur_result = murmur.predict(np.array(data1))
y1 = af_result[0]
b1 = murmur_result[0]

af_result = af.predict(np.array(data2))
murmur_result = murmur.predict(np.array(data2))
y2 = af_result[0]
b2 = murmur_result[0]

#Make it in % instead of 0.
af_return = y1[0]*100
murmur_return = b1[0]*100
#Show the ai confidence[AF,murmur]
print('File 1: ',[af_return, murmur_return])

af_return = y2[0]*100
murmur_return = b2[0]*100
print('File 2: ',[af_return, murmur_return])