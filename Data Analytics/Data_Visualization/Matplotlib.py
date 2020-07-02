
## link for reference - https://matplotlib.org/tutorials/introductory/sample_plots.html
#                       https://seaborn.pydata.org/examples/index.html
#                       https://seaborn.pydata.org/tutorial.html

'''
Matplotlib is an interactive python graph-plotting library that helps us visualize data in various 2D plots.
The following is an example of how matplotlib can be used to create a visualization of the Sin wave.
'''

import numpy as np
import matplotlib.pyplot as plt


# Get x values of the sine wave
points = np.arange(0, 10, 0.1);

# Plot a sine wave
plt.plot(points, np.sin(points))

# Give a title for the sine wave plot
plt.title('Sine wave')

# Give x axis label for the sine wave plot
plt.xlabel('Time')

# Give y axis label for the sine wave plot
plt.ylabel('Amplitude')

plt.show()