import sys
import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as signal
from scipy.signal import find_peaks

data = []
f = sys.stdin.readline().rstrip()
order = 3
freq = 0.3
while f:
    data.append(int(f))
    f = sys.stdin.readline().rstrip()

df = pd.DataFrame(data)
b, a = signal.bessel(order, freq)
x = signal.filtfilt(b, a, data)
peaks, _ = find_peaks(x)
print(peaks.size)

plt.plot(x)
plt.plot(data)
plt.show()
