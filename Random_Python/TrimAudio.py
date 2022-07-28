from scipy.io import wavfile
 
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])
 
 
trim_wav("C:/Users/mattc/OneDrive/Documents/Project/CSM/Testing/MicTest/A51/Redmi Bud 3 lite/BudTest3.wav", 0,10)