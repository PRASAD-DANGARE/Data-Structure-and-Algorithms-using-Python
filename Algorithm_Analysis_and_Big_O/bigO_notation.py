import numpy as np
import matplotlib.pyplot as plt

# Use a style for the plot
plt.style.use('bmh')

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
labels = ['Constant_O(1)', 'Logarithmic_O(logn)', 'Linear_O(n)', 'LogLinear_O(nlogn)', 'Quadratic_O(n2)', 'Cubic_O(n3)', 'Exponential_O(2n)']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n ** 2, n ** 3, 2 ** n]

# Plot setup
plt.figure(figsize=(12, 10))
plt.ylim(0, 50)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.show()
