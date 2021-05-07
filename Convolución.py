#Se importa las bibliotecas que se usarán
import os
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


Matriz = np.array([[1,1,1,1], [1,1,1,1], [0,0,0,0], [0,0,0,0]])
Kernel = np.array([[1,1], [-1,-1]])
Matriz


temp = signal.convolve2d(Matriz, Kernel, mode='same')
print(temp)
