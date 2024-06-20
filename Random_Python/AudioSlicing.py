import os
import glob
import numpy as np
from scipy.io import wavfile

time = 5

# Path to the folder containing the .wav files
input_folder = 'C:/Users/matt_c/Documents/Projects/CS-M/Datasets/AAAdataset/af/train'

# Path to the folder where the sliced audio files will be saved
output_folder = 'C:/Users/matt_c/Documents/Projects/CS-M/Datasets/10Sec/AF'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all .wav files in the input folder
wav_files = glob.glob(os.path.join(input_folder, '*.wav'))
x = 94
# Iterate over each .wav file
for wav_file in wav_files:
    x += 1
    # Load the .wav file
    sample_rate, audio_data = wavfile.read(wav_file)
    
    # Calculate the duration of the audio file in seconds
    duration = len(audio_data) / sample_rate
    
    # Check if the duration is at least 10 seconds
    if duration >= time:
        # Calculate the number of slices
        num_slices = int(duration / time)
        
        # Iterate over each slice
        for i in range(num_slices):
            # Calculate the start and end indices of the slice
            start_index = i * time * sample_rate
            end_index = (i + 1) * time * sample_rate
            
            # Extract the slice from the audio data
            slice_data = audio_data[start_index:end_index]

            # Check if the slice duration is at least 10 seconds
            if len(slice_data) >= time * sample_rate:
                # Save the slice as a new .wav file
                output_file = os.path.join(output_folder, f'{x}({i+1}).wav')
                wavfile.write(output_file, sample_rate, slice_data)