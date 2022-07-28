import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
# Define Transfer Function
num = np.array([6])
den = np.array([6 , 1])
H = signal.TransferFunction(num, den)
print ('H(s) =', H)
# Frequencies
w_start = 0.01
w_stop = 10
step = 0.01
N = int ((w_stop-w_start )/step) + 1
w = np.linspace (w_start , w_stop , N)
# Bode Plot
w, mag, phase = signal.bode(H, w)
plt.semilogx(w, mag) # Bode Magnitude Plot
plt.title("Bode Plot")
plt.grid(b=None, which='major', axis='both')
plt.grid(b=None, which='minor', axis='both')
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency (rad/sec)")
plt.show()