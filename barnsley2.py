import random
import matplotlib.pyplot as plt

def barnsley_fern(iterations):
    x, y = 0, 0
    x_list, y_list = [x], [y]

    for _ in range(iterations):
        r = random.uniform(0, 100)
        if r < 1:
            x, y = 0, 0.16 * y
        elif r < 86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

        x_list.append(x)
        y_list.append(y)

    return x_list, y_list

def plot_barnsley_fern(iterations):
    x_list, y_list = barnsley_fern(iterations)
    plt.scatter(x_list, y_list, s=0.2, color='green')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    plot_barnsley_fern(10000)