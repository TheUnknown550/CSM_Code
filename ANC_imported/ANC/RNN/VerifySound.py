import numpy as np
import librosa
from sklearn.model_selection import train_test_split

def load_audio_file(file_path, duration=10):
    audio, sr = librosa.load(file_path, duration=duration)
    return audio, sr

def segment_audio(audio, window_size, hop_size):
    frames = librosa.util.frame(audio, frame_length=window_size, hop_length=hop_size)
    return frames

def extract_features(segment, sr):
    features = librosa.feature.melspectrogram(segment, sr=sr, n_mels=128, hop_length=256)
    return features

heart_audio, sr = load_audio_file('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Heart/normal/(1).wav    ')
window_size = 256
hop_size = window_size // 2

heart_segments = segment_audio(heart_audio, window_size, hop_size)

input_data = np.array([extract_features(segment, sr) for segment in heart_segments])

# Check the shapes of input_data
print("input_data shape:", input_data.shape)

target_data = np.array([segment for segment in heart_segments])

# Check the shapes of target_data
print("target_data shape:", target_data.shape)

time_steps = 5

X_train, X_test, y_train, y_test = train_test_split(input_data, target_data, test_size=0.2, random_state=42)

num_samples_train = X_train.shape[0]
X_train = X_train.reshape(num_samples_train, time_steps, X_train.shape[1] // time_steps)

num_samples_test = X_test.shape[0]
X_test = X_test.reshape(num_samples_test, time_steps, X_test.shape[1] // time_steps)
