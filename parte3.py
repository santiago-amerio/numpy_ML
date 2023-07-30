import matplotlib.pyplot as plt
import numpy as np
import math

def ejercicio_1():
    def y_func(x):
        return 3 * x - 2

    x = np.arange(-10, 10, 0.1)
    y = y_func(x)

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("3 * x - 2")
    plt.show()


def ejercicio_2():
    def y_func(x):
        return 2 * x**2 + 4 * x + 2

    x = np.arange(-10, 10, 1)

    y = y_func(x)
    print(x)
    print(y)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("2 * x**2 + 4 * x + 2")
    plt.show()


def ejercicio_3():
    def y_func(x):
        return abs(x)

    x = np.arange(-10, 10, 0.1)
    y = y_func(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("abs x")
    plt.show()


def ejercicio_4():
    def y_func(x):
        return 1 / x

    x = np.arange(-10, 10, 1)
    y = y_func(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("1/x")
    plt.show()



def ejercicio_4():
    def y_func(x):
        return np.sqrt(x)

    x = np.arange(0, 10, .01)
    y = y_func(x)
    print(x)
    print(y)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("sqrt(x)")
    plt.show()


