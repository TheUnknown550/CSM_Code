import soundfile as sf
import numpy as np
from scipy import signal
import librosa
from pydub import AudioSegment

# Read the first audio file
sound1 = AudioSegment.from_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Original/All/(1).wav')

# Read the second audio file
sound2 = AudioSegment.from_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Noise_Clip_2.wav')


combined = sound1.overlay(sound2)

combined.export("C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/MixedSound.wav", format='wav')