#!/usr/bin/python
import math
import matplotlib.pyplot as plt
import scipy as sp


def getKoef(x, y):
    if len(x) != len(y):
        return "error"
    n = len(x)
    a_numerator = n * math.fsum(map(lambda x, y: x * y, x, y)) - math.fsum(x) * math.fsum(y)
    a_denominator = math.fsum(map(lambda x: x * x, x)) * n - math.fsum(x) ** 2
    a = a_numerator / a_denominator

    b = (math.fsum(y) - a * math.fsum(x)) / n
    print(a, b)
    return a, b


def make_function(a, b):
    return lambda x: a * x + b


data = sp.genfromtxt("data.tsv", delimiter="\t")

x = data[:, 0]
y = data[:, 1]

f = make_function(1, 1)(2)
arg = getKoef(x, y)
a = make_function(arg[0], arg[1])
range_x = range(int(min(x)) - 10, int(max(x)) + 10)
function = [a(x) for x in range_x]

plt.plot(range_x, function)
plt.scatter(x, y)
plt.grid()
plt.show()
