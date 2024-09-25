#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

print("Hello world")


#name = input("Enter Name: ")

#print("Hello " + name + "!")

x = np.array([x for x in range(20)])

y = x**2

plt.plot(x,y)
plt.savefig("plot_example.png")


