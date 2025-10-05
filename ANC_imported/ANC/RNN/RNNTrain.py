import numpy as np
import librosa
import soundfile
from keras.layers import Input, Dense, LSTM
from keras.models import Model
from sklearn.model_selection import train_test_split
import math
import warnings
warnings.filterwarnings("ignore")

def load_audio_file(file_path, duration=10):
    audio, sr = librosa.load(file_path, sr=None, mono=True, duration=duration)
    return audio, sr

def segment_audio(audio, window_size, hop_size):
    frames = librosa.util.frame(audio, frame_length=window_size, hop_length=hop_size).T
    return frames

def extract_features(audio, sr):
    features = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128, hop_length=256)
    return features.T



# Load Heart Sound and Noise files and mix them to create Mixed file
heart_audio ,sr = load_audio_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Heart/normal/(1).wav')
noise_audio , _= load_audio_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Noise/(1).wav')
mixed_audio , _= load_audio_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/MixedSounds/Sound(1)/normal/(1).wav')

window_size = 1024
hop_size = 256

heart_segments = segment_audio(heart_audio, window_size, hop_size)
noise_segments = segment_audio(noise_audio, window_size, hop_size)
mixed_segments = segment_audio(mixed_audio, window_size, hop_size)

min_segments = min(len(heart_segments), len(noise_segments), len(mixed_segments))

heart_segments = heart_segments[:min_segments]
noise_segments = noise_segments[:min_segments]
mixed_segments = mixed_segments[:min_segments]

heart_features = np.array([extract_features(segment, sr) for segment in heart_segments])
noise_features = np.array([extract_features(segment, sr) for segment in noise_segments])
mixed_features = np.array([extract_features(segment, sr) for segment in mixed_segments])

input_data = np.hstack((mixed_features, noise_features))
target_data = heart_features

X_train, X_test, y_train, y_test = train_test_split(input_data, target_data, test_size=0.2, random_state=42)

num_samples = X_test.shape[0]

time_steps = 5
X_train = X_train.reshape(-1, time_steps, X_train.shape[1])
X_test = X_test.reshape(num_samples, time_steps, X_test.shape[1] // time_steps)
y_train = y_train.reshape(-1, time_steps, y_train.shape[1])
y_test = y_test.reshape(-1, time_steps, y_test.shape[1])

input_layer = Input(shape=(time_steps, X_train.shape[2]))
x = LSTM(64, return_sequences=True)(input_layer)
x = LSTM(64, return_sequences=True)(x)
output_layer = Dense(y_train.shape[2], activation='linear')(x)

model = Model(input_layer, output_layer)
model.compile(optimizer='adam', loss='mse')

model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

denoised_heart_features = model.predict(mixed_features.reshape(-1, time_steps, mixed_features.shape[1]))

def features_to_audio(features, sr):
    features = features.T
    audio = librosa.feature.inverse.mel_to_audio(features, sr=sr, hop_length=256)
    return audio


denoised_heart_audio = np.concatenate([features_to_audio(segment, sr) for segment in denoised_heart_features])

soundfile.write("denoised_heart_file.wav", denoised_heart_audio, sr)

# Filter Effectiveness Tests
# Calculate the Noise% (High is good)
# Trim the ANC array to match the length of the Test array
denoised_heart_audio = denoised_heart_audio[:len(heart_audio)]
        
# Calculate SNR
signal_power = np.mean(np.square(heart_audio))
noise_power = np.mean(np.square(denoised_heart_audio - heart_audio))
if noise_power == 0:
    SNR = float('inf')  # infinite SNR for zero noise power
else:
    SNR = 10 * math.log10(signal_power / noise_power)
print('SNR: ',SNR)

# Calculate the MSE (low is good)
RMSE = np.sqrt(np.mean(np.square(heart_audio - denoised_heart_audio)))
print('RMSE: ',RMSE)