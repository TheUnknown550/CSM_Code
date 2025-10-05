import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import soundfile as sf
import openpyxl as px
from scipy.signal import firwin, filtfilt
from pydub import AudioSegment
import time

for n in range(13):
    for i in range(40):
        # Trim the Audio
        def trim_wav( originalWavPath, start, end, name ):
            sampleRate, waveData = wavfile.read( originalWavPath )
            startSample = int( start * sampleRate )
            endSample = int( end * sampleRate )
            wavfile.write( name, sampleRate, waveData[startSample:endSample])

        # Trim Audio File to 10 sec
        if n < 7:
            trim_wav("C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Heart/normal/("+str(i+1)+").wav", 0,10, 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Original.wav')
            trim_wav("C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Noise/("+str(n+1)+").wav", 0,10, 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Noise.wav')
            Output = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/MixedSounds/'+str(n+1)+'00Hz/normal/('+str(i+1)+').wav'
        else:
            trim_wav("C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Heart/murmur/("+str(i+1)+").wav", 0,10, 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Original.wav')
            trim_wav("C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Noise/("+str(n-6)+").wav", 0,10, 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Noise.wav')
            Output = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/MixedSounds/'+str(n-6)+'00Hz/murmur/('+str(i+1)+').wav'
        
        # Read the first audio file
        sound1 = AudioSegment.from_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Original.wav')
        sound2 = AudioSegment.from_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Noise.wav')

        combined = sound1.overlay(sound2)

        combined.export(Output, format='wav')
        print('File Done!!'+str(i+1))