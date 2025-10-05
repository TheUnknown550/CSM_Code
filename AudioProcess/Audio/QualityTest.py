import soundfile as sf
from scipy import signal
import math
import numpy as np

# Load two sound files
sound1, sample_rate1 = sf.read('C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/normal/0dB/(9).wav')
sound2, sample_rate2 = sf.read('C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/normal/10dB/(9s).wav')

# Resample if necessary
if sample_rate1 != sample_rate2:
    resampled_sound2 = signal.resample(sound2, len(sound1))
else:
    resampled_sound2 = sound2

# Calculate the SNR
signal_power = np.sum(sound1 ** 2)
noise_power = np.sum((sound1 - resampled_sound2) ** 2)
snr = 10 * math.log10(signal_power / noise_power)

# Calculate the RMSE
mse = np.mean((sound1 - resampled_sound2) ** 2)
rmse = math.sqrt(mse)

# Print the results
print("SNR: {:.2f} dB".format(snr))
print("RMSE: {:.4f}".format(rmse))
