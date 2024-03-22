import numpy as np
import matplotlib.pyplot as pyp

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = pyp.hist(x, 50, density=True, facecolor='g', alpha=0.75)


pyp.xlabel('Smarts')
pyp.ylabel('Probability')
pyp.title('Histogram of IQ')
pyp.text(60, .025, r'$\mu=100,\ \sigma=15$')
pyp.axis([40, 160, 0, 0.03])
pyp.grid(True)
pyp.show()