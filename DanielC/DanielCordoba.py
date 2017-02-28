from __future__ import division #only for Python 2.7
import numpy as np
import matplotlib.pyplot as plt # matplotlib inline
import time
figureName = time.strftime("%Y%m%d-%H%M%S") #File name

# simulate EMG signal
burst1 = np.random.uniform(-1, 1, size=1000) + 0.08
burst2 = np.random.uniform(-1, 1, size=1000) + 0.08
quiet = np.random.uniform(-0.05, 0.05, size=500) + 0.08
emg = np.concatenate([quiet, burst1, quiet, burst2, quiet])
time = np.array([i/1000.0 for i in range(0, len(emg), 1)]) # sampling rate 1000 Hz

# plot EMG signal
fig = plt.figure()
plt.plot(time, emg)
plt.xlabel('Time (mili-sec)')
plt.ylabel('EMG (a.u.)')
fig_name = figureName + '.png'
fig.set_size_inches((11, 7))
fig.savefig(fig_name)
print 'output file name: ', fig_name
