import random
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import gca


def multiply_matrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("you can't multiply them, due to their size")
        return
    else:
        new_matrix = []
        for _ in range(len(matrix1)):
            new_matrix.append([0 for x in range(len(matrix2[0]))])
        for row_i, row in enumerate(matrix1):
            for col in range(len(matrix2[0])):
                sum = 0
                for ind in range(len(row)):
                    # print(row[ind], "*", matrix2[ind][col])
                    sum += row[ind] * matrix2[ind][col]
                new_matrix[row_i][col] = sum
    return new_matrix

n_list = []
for v in range(9):
    n_list.append(2 ** v)
res_time = []
for n in n_list:
    matrix1 = np.zeros((n, n), dtype=int)
    matrix2 = np.zeros((n, n), dtype=int)
    for x in range(n):
        for y in range(n):
            matrix1[x][y] = random.randint(1, 50)
            matrix2[x][y] = random.randint(1, 50)
    time1 = time.time()
    multiply_matrix(matrix1, matrix2)
    time2 = time.time()
    res_time.append(time2 - time1)
print(n_list)
plt.plot(n_list, res_time)
plt.title("Strassen Matrices Multiplication")
plt.xlabel("matrix size")
plt.show()
new_time = []
for elem in res_time:
    new_time.append(elem ** (1/3))
plt.plot(n_list, new_time)
plt.title("O(n^3) complexity check")
plt.xlabel("matrix size")
plt.show()
