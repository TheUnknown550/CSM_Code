from scipy.io import wavfile
import soundfile as sf

# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])

# Automation
for i in range (1000):
    print(i+1)
    # Load the audio file
    trim_wav('C:/Users/Matt/Documents/Project/CS-M/Experiments/AmpLowTests/normal/LowToAmp/LowAudio1/('+str(i+1)+').wav', 0,10)
    frames, sample_rate = sf.read('File.wav')

    # Increase the desired decibel level
    Amplified_frames = frames*3


    # Export new WAV file
    sf.write('C:/Users/Matt/Documents/Project/CS-M/Experiments/AmpLowTests/normal/LowToAmp/AmpAudio2/('+str(i+1)+').wav', Amplified_frames, sample_rate)
