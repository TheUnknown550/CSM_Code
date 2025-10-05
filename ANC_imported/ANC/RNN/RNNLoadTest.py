import tensorflow as tf
import librosa
import numpy as np

# Load the mixed sound (Sound1) and the new noise sound (NewNoise)
mixed_sound, sr = librosa.load('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/MixedSounds/Sound(1)/normal/(1).wav', sr=16000)
new_noise_sound, sr = librosa.load('NewNoise.wav', sr=16000)

# Extract features from the mixed sound
mixed_sound_stft = librosa.stft(mixed_sound, n_fft=1024, hop_length=512)
mixed_sound_mag = np.abs(mixed_sound_stft)
mixed_sound_phase = np.angle(mixed_sound_stft)

# Extract features from the new noise sound
new_noise_sound_stft = librosa.stft(new_noise_sound, n_fft=1024, hop_length=512)
new_noise_sound_mag = np.abs(new_noise_sound_stft)

# Load the existing RNN model
model = tf.keras.models.load_model('rnn_model.h5')

# Apply the active noise cancelling to the mixed sound
mixed_sound_stft = mixed_sound_stft.reshape(1, mixed_sound_stft.shape[0], mixed_sound_stft.shape[1])
mixed_sound_mag = np.abs(mixed_sound_stft)
predicted_noise_sound_mag = model.predict(mixed_sound_mag)
predicted_noise_sound_mag = predicted_noise_sound_mag.reshape(predicted_noise_sound_mag.shape[1], predicted_noise_sound_mag.shape[2])
predicted_noise_sound_stft = predicted_noise_sound_mag * np.exp(1j * mixed_sound_phase)

# Subtract the estimated noise from the mixed sound
cleaned_sound_stft = mixed_sound_stft - predicted_noise_sound_stft

# Reconstruct the cleaned audio
cleaned_sound = librosa.istft(cleaned_sound_stft, hop_length=512)

# Save the cleaned audio
librosa.output.write_wav('cleaned_sound.wav', cleaned_sound, sr)
