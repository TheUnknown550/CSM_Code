import soundfile as sf
import numpy as np
import math

# Load the audio file using soundfile
audio_data, sample_rate = sf.read("C:/Users/Matt/Documents/Project/CS-M/Datasets/Testing/Noises/50dB.wav")

# Get the peak level of the audio data
peak_level = np.max(np.abs(audio_data))

# Print the peak level in decibels (dB)
print(f"Peak level: {20 * math.log10(peak_level):.2f} dB")
