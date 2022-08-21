X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
fig, ax = plt.subplots()
D_highres = librosa.stft(x, hop_length=256, n_fft=4096)
S_db_hr = librosa.amplitude_to_db(np.abs(D_highres), ref=np.max)
img = librosa.display.specshow(S_db_hr, hop_length=256, x_axis='time', y_axis='log',ax=ax)
ax.set(title='Higher time and frequency resolution')
fig.colorbar(img, ax=ax, format="%+2.f dB")
plt.show()