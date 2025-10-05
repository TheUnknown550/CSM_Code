import soundfile as sf
import numpy as np
import librosa
from scipy.io import wavfile

# File Number
for n in range(40):

    # Trim the Audio
    def trim_wav( originalWavPath, start, end, name ):
        sampleRate, waveData = wavfile.read( originalWavPath )
        startSample = int( start * sampleRate )
        endSample = int( end * sampleRate )
        wavfile.write( name, sampleRate, waveData[startSample:endSample])
    
    # Trim and Load the audio file
    trim_wav(f"C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests2/Control/normal/({n+1}).wav", 0,10, 'File.wav')
    data1, sample_rate1 = sf.read('File.wav')
    current_db1= 20 * np.log10(np.sqrt(np.mean(data1 ** 2)))
    print('dB1: ', current_db1)


    # Load the second audio file
    trim_wav("C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests2/Noise/Water.wav", 0,10, 'Noise.wav')
    data2, sample_rate2 = sf.read('Noise.wav')
    current_db2 = 20 * np.log10(np.sqrt(np.mean(data2 ** 2)))
    print('dB2: ', current_db2)


    # Convert stereo signals to mono if necessary
    if data1.ndim > 1:
        data1 = np.mean(data1, axis=1)
    if data2.ndim > 1:
        data2 = np.mean(data2, axis=1)

    # Resample the audio files if they have different sample rates
    if sample_rate1 != sample_rate2:
        print('Resampling audio files...')
        if sample_rate1 > sample_rate2:
            data1 = data1[::int(sample_rate1/sample_rate2)]
            sample_rate1 = sample_rate2
        else:
            data2 = data2[::int(sample_rate2/sample_rate1)]
            sample_rate2 = sample_rate1

    # Make the two signals the same length
    length = min(len(data1), len(data2))
    data1 = data1[:length]
    data2 = data2[:length]

    # Mix the two audio signals
    mixed_data = (data1 + data2)
    # Normalize the mixed signal
    #mixed_data_normalized = mixed_data / np.max(np.abs(mixed_data))

    # Write the mixed audio to a new file
    sf.write('C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests2/Mixed/Water/('+str(n+1)+').wav', mixed_data, sample_rate1)