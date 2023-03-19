import random
import matplotlib.pyplot as plt

# Define the four transformations for the fern
def f1(x, y):
    return 0, 0.16*y

def f2(x, y):
    return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6

def f3(x, y):
    return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6

def f4(x, y):
    return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

# Set the initial point to (0, 0)
x, y = [0], [0]

# Generate the points for the fern using one of the four transformations randomly chosen with a probability
# proportional to its associated weight.
for i in range(100000):
    r = random.random()
    if r <= 0.01:
        x.append(f1(x[-1], y[-1])[0])
        y.append(f1(x[-2], y[-2])[1])
    elif r   <= 0.86:
        x.append(f2(x[-1], y[-1])[0])
        y.append(f2(x[-2], y[-2])[1])
    elif r <= 0.93:
        x.append(f3(x[-1], y[-1])[0])
        y.append(f3(x[-2], y[-2])[1])
    else:
        x.append(f4(x[-1], y[-1])[0])
        y.append(f4(x[-2], y[-2])[1])

# Plot the points to generate the Barnsley fern fractal pattern
plt.scatter(x, y, s=5)
plt.show()