import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(1, 1, 1, polar=True)

def mapr(r):
   """Remap the radial axis."""
   return 90 - r

r = np.arange(0, 90, 0.01)
theta = 2 * np.pi * r / 90

ax.plot(theta, mapr(r))
ax.set_yticks(range(0, 90, 10))                   # Define the yticks
ax.set_yticklabels(map(str, range(90, 0, -10)))   # Change the labels
plt.show()