from math import *
def func1 (x1):
    y = ((sin(x1) - log10(x1)) / sqrt(7 * x1)) + (x1 + 4)**(2 * x1 - 8)
    return(y)
x = float(input("Введіть значення х:"))
y = func1 (x)
print(y)