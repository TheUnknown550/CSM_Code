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

af = load_model('C:/Users/Matt/Documents/Project/CS-M/CS-M_Code-ENVY/AI/Models/AF.h5')#AF AI Path
murmur = load_model('C:/Users/Matt/Documents/Project/CS-M/CS-M_Code-ENVY/AI/Models/murmur.h5') #murmur AI Path

#variables
mfccs = 0.0
data = []
result = []
file_name = 'C:/Users/Matt/Documents/Project/CS-M/Datasets/murmur/test/(2).wav' #WAV File Path

#Extract and read the WAV file for the AI
a = extract_data(file_name)
data.append(a)

#Analize Predict and Save the data
af_result = af.predict(np.array(data))
murmur_result = murmur.predict(np.array(data))
y = af_result[0]
b = murmur_result[0]

#Make it in % instead of 0.
af_return = y[0]*100
murmur_return = b[0]*100

#Show the ai confidence[AF,murmur]
returnvalue = [af_return, murmur_return]
print(returnvalue)
