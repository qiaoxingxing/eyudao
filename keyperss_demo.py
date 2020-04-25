
import sys
import numpy as np
import matplotlib.pyplot as plt


def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == ' ':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        ax.plot(np.random.rand(1), np.random.rand(1),'r^')
        fig.canvas.draw()

# Fixing random state for reproducibility
np.random.seed(19680801)



fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', press)

circle = plt.Circle((0, 0), 5, color='g')
ax.add_artist(circle)

ax.axis([-10, 10,- 10, 10])
ax.set_aspect('equal', adjustable='box', anchor='C')

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()