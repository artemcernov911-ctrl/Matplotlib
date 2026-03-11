import numpy as np
import matplotlib.pyplot as plt

random_array = np.random.rand(5)

plt.scatter(random_array, random_array)
plt.title('scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

