import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib

fname = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/AITest/A22/Test11.wav'
outname1 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile1.wav'
outname2 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile2.wav'
outname3 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile3.wav'
outname4 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile4.wav'
outname5 = 'C:/Users/mattc/OneDrive/Documents/Project/CSM/HeartDiseaseSounds/ReducNoise_Testing/TestFile5.wav'

cutOffFrequency1 = 10.0
cutOffFrequency2 = 20.0
cutOffFrequency3 = 30.0
cutOffFrequency4 = 40.0
cutOffFrequency5 = 50.0

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

with contextlib.closing(wave.open(fname,'rb')) as spf:
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
    freqRatio1 = (cutOffFrequency1/sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio1**2)/freqRatio1)

    # Use moviung average (only on first channel)
    filtered = running_mean(channels[0], N).astype(channels.dtype)

    wav_file1 = wave.open(outname1, "w")
    wav_file1.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file1.writeframes(filtered.tobytes('C'))
    wav_file1.close()


    #100.0 cutoff
    freqRatio2 = (cutOffFrequency2/sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio2**2)/freqRatio2)

    # Use moviung average (only on first channel)
    filtered = running_mean(channels[0], N).astype(channels.dtype)

    wav_file2 = wave.open(outname2, "w")
    wav_file2.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file2.writeframes(filtered.tobytes('C'))
    wav_file2.close()


    #200.0 cutoff
    freqRatio3 = (cutOffFrequency3/sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio3**2)/freqRatio3)

    # Use moviung average (only on first channel)
    filtered = running_mean(channels[0], N).astype(channels.dtype)

    wav_file3 = wave.open(outname3, "w")
    wav_file3.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file3.writeframes(filtered.tobytes('C'))
    wav_file3.close()


    #300.0 cutoff
    freqRatio4 = (cutOffFrequency4/sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio4**2)/freqRatio4)

    # Use moviung average (only on first channel)
    filtered = running_mean(channels[0], N).astype(channels.dtype)

    wav_file4 = wave.open(outname4, "w")
    wav_file4.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file4.writeframes(filtered.tobytes('C'))
    wav_file4.close()


    #400.o cutoff
    freqRatio5 = (cutOffFrequency5/sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio5**2)/freqRatio5)

    # Use moviung average (only on first channel)
    filtered = running_mean(channels[0], N).astype(channels.dtype)

    wav_file5 = wave.open(outname5, "w")
    wav_file5.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file5.writeframes(filtered.tobytes('C'))
    wav_file5.close()