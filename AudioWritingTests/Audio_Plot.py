import audio_plot as ap
import numpy as np

sin = np.sin(np.arange(0, np.pi*2, 0.1))  # 0,  0.09983342,  0.19866933,  0.29552021,  0.38941834, ...
two_inverted_sin = np.array([sin, -1 * sin]).T

# generate graph sound
audio = ap.plot(two_inverted_sin)

# save to audio file
audio.export("graph.wav", format="wav")
print('Done!!')
