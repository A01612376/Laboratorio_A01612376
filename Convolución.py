#Se importa las bibliotecas que se usarán
import os
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Se crea matriz de 4x4 y un kernel de 2x2
Matriz = np.array([[1,1,1,1], [1,1,1,1], [0,0,0,0], [0,0,0,0]])
Kernel = np.array([[1,1], [-1,-1]])
Matriz

#Se llama la función de convulción y se pasa la matriz de entrada
temp = signal.convolve2d(Matriz, Kernel, mode='same')
print(temp)






