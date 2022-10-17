from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Calculating the order and the cut-off frequency
N, Wn = signal.cheb1ord(100, 200, .5, 20, True)

# Calculating the Pole-Zero Locations
for i in range(1, 7):
    N = i
    z, p, k = signal.cheby1(N, .35, Wn, 'low', True, 'zpk')

    # Frequency Response

    w, h = signal.freqs_zpk(z, p, k, 100)
    plt.semilogx(w, 20 * np.log10(abs(h)))

plt.title('Chebyshev-I filter frequency response (n=1 to 6)')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='red')  # cutoff frequency
plt.show()


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


# w, h = signal.freqs(b, a)
# ax2.semilogx(w, 20 * np.log10(abs(h)))
# ax2.set_title('Butterworth filter frequency response')
# ax2.set_xlabel('Frequency [radians / second]')
# ax2.set_ylabel('Amplitude [dB]')
# ax2.margins(0, 0.1)
# ax2.grid(which='both', axis='both')
# ax2.axvline(100, color='green')  # cutoff frequency


# fig.tight_layout()
