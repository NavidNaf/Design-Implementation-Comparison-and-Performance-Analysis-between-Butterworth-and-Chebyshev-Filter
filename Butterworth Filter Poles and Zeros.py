from scipy import signal
import matplotlib.pyplot as plt

z, p, k = signal.butter(5, 123.41, btype='low', analog=True,
                        output='zpk', fs=None)
print(z)
print(p)
print(k)
