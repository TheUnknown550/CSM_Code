import numpy as np
from scipy.signal import find_peaks, butter, hilbert, filtfilt
from scipy.io import wavfile
import pandas as pd
import os

def homomorphic_envelope(y, fs, f_LPF=8, order=3):
    if fs <= 0:
        raise ValueError("Sampling rate (fs) must be greater than zero")
    if f_LPF <= 0 or f_LPF >= fs / 2:
        raise ValueError("Low-pass filter frequency (f_LPF) must be between 0 and fs/2")
    
    b, a = butter(order, 2 * f_LPF / fs, 'low')  # Design the filter
    he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y)))))  # Apply the filter to the signal
    return he

def AFCounter(filename):
    try:# check if file can be read
        fs, y = wavfile.read(filename)  # Load audio
        if y.ndim > 1:  # If stereo, take one channel
            y = y[:, 0]
    except Exception as e:
        print(f"Error loading audio file: {e}")
        raise

    try:#check if theres an error if not run normally
        he = homomorphic_envelope(y, fs)
    except ValueError as e:
        print(f"Error: {e}")
        raise

    peaks, _ = find_peaks(he, height=np.quantile(he, 0.8))  # Detect the highest peaks of the peaks
    distance = np.diff(peaks)  # Calculate the distance between the peaks
    #print("Distance: ", distance)

    # locate the short and long distances that shows when is the S1 and S2 sounds are, if the distanecs varies too much then its AF
    prev = 0 # record the previous distance
    ShortLong = [] # Record the short and long distances Short = 0, Long = 1
    for i in distance:
        if i <= prev and prev!= 0:  # Check if the distance is an outlier
            ShortLong.append(0)
        elif i >= prev and prev!= 0:
            ShortLong.append(1)
        prev = i

    print(ShortLong)

    prev = 2 # if the shorts and shorts are together Will add 1 to AF and record the amount of AFs detected
    AF = 0
    for i in ShortLong:
        if i == prev:
            AF += 1
        else:
            prev = i

    return AF


def read_files(directory):
    i = 0
    # Initialize an empty list to store the data
    data = []
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.wav'):
            # Construct the full file path
            filepath = os.path.join(directory, filename)

            AF = AFCounter(filepath)

            i+=1# Record the numbers of files

            # Append the details to the data list
            data.append({
                'FileNum': i,
                'AF Count': AF,
            })
    return pd.DataFrame(data)
            
# Define the directory containing the .wav files
directory1 = 'C:/Users/matt_c/Documents/Projects/CS-M/Datasets/10Sec/AF'
directory2 = 'C:/Users/matt_c/Documents/Projects/CS-M/Datasets/10Sec/Normal'

# Read .wav files from both directories
df1 = read_files(directory1)
df2 = read_files(directory2)

# Create a Pandas Excel writer using XlsxWriter as the engine
output_file = 'C:/Users/matt_c/Documents/Projects/CS-M/Code/Excels/AFAlgorTest.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write each DataFrame to a separate sheet
    df1.to_excel(writer, sheet_name='AF', index=False)
    df2.to_excel(writer, sheet_name='Normal', index=False)

print(f'Data has been written to {output_file}')