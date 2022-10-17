from numpy.core.defchararray import equal
from numpy.lib.type_check import imag
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

z, p, k = signal.butter(5, 123.41, btype='low', analog=True,
                        output='zpk', fs=None)
print(z)
print(p)
print(k)


def plotPoleZeros(zeros=[], poles=[]):
    fig, ax = plt.subplots()

    # Unit Circle Draw
    theta = np.linspace(0, 2*np.pi, 100)
    ejtheta = np.exp(1j*theta)
    plt.plot(np.imag(ejtheta), np.real(ejtheta))

    # Zeros
    for pt in zeros:
        plt.plot(np.imag(pt), np.real(pt), "ro")

    # Poles
    for pt in poles:
        plt.plot(np.imag(pt), np.real(pt), "rx")

    plt.grid()
    ax.set_aspect("equal", adjustable="datalim")
    plt.show()


plotPoleZeros(z, p)
