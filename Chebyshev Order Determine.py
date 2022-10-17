from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Calculating the order and the cut-off frequency
N1, Wn1 = signal.cheb1ord(100, 200, .5, 20, True)
N2, Wn2 = signal.buttord(100, 200, .5, 20, True)

# Calculating the Pole-Zero Locations
z1, p1, k1 = signal.cheby1(N1, .35, Wn1, 'low', True, 'zpk')
z2, p2, k2 = signal.butter(N1, Wn1, 'low', True, 'zpk')

# Frequency Response
w1, h1 = signal.freqs_zpk(z1, p1, k1)
plt.semilogx(w1, 20 * np.log10(abs(h1)))
w2, h2 = signal.freqs_zpk(z2, p2, k2)
plt.semilogx(w2, 20 * np.log10(abs(h2)))

plt.title('Butterworth vs. Chebyshev Type I frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green')  # cutoff frequency
plt.axhline(-5, color='green')  # rp
plt.show()

# print(k)
# b, a = signal.cheby1(4, .35, 100, 'low', analog=True)

# def plotPoleZeros(zeros=[], poles=[]):
#     fig, ax = plt.subplots()
#     plt.title("Poles and Zeros Mapping")

#     # Unit Circle Draw
#     theta = np.linspace(0, 2*np.pi, 100)
#     ejtheta = np.exp(1j*theta)
#     plt.plot(np.real(ejtheta), np.imag(ejtheta))

#     # Zeros
#     for pt in zeros:
#         plt.plot(np.real(pt), np.imag(pt), "ro")

#     # Poles
#     for pt in poles:
#         plt.plot(np.real(pt), np.imag(pt), "rx")

#     plt.grid()
#     ax.set_aspect("equal", adjustable="datalim")
#     plt.show()


# plotPoleZeros(z, p)
