import time
import random

import numpy as np
from matplotlib import pyplot as plt


def strassen_mult(matrix1, matrix2):
    if matrix1.size == 1 or matrix2.size == 1:
        return matrix1 * matrix2

    col_len = matrix1.shape[0]
    # if len of column is an odd number
    if col_len % 2 != 0:
        # matrix padding
        matrix1 = np.pad(matrix1, (0, 1), mode='constant')
        matrix2 = np.pad(matrix2, (0, 1), mode='constant')

    delimeter = int(np.ceil(col_len / 2))
    # slice matrix in 8 pieces
    slice1 = matrix1[:delimeter, :delimeter]
    slice2 = matrix1[:delimeter, delimeter:]
    slice3 = matrix1[delimeter:, :delimeter]
    slice4 = matrix1[delimeter:, delimeter:]
    slice5 = matrix2[:delimeter, :delimeter]
    slice6 = matrix2[:delimeter, delimeter:]
    slice7 = matrix2[delimeter:, :delimeter]
    slice8 = matrix2[delimeter:, delimeter:]

    part1 = strassen_mult(slice1, slice6 - slice8)
    part2 = strassen_mult(slice1 + slice2, slice8)
    part3 = strassen_mult(slice3 + slice4, slice5)
    part4 = strassen_mult(slice4, slice7 - slice5)
    part5 = strassen_mult(slice1 + slice4, slice5 + slice8)
    part6 = strassen_mult(slice2 - slice4, slice7 + slice8)
    part7 = strassen_mult(slice1 - slice3, slice5 + slice6)

    # full matrix with '0'
    res = np.zeros((2 * delimeter, 2 * delimeter), dtype=np.int32)
    # print(res)
    res[:delimeter, :delimeter] = part5 + part4 - part2 + part6
    res[:delimeter, delimeter:] = part1 + part2
    res[delimeter:, :delimeter] = part3 + part4
    res[delimeter:, delimeter:] = part1 + part5 - part3 - part7
    return res[:col_len, :col_len]


n_list = [2, 20, 100, 400, 700, 1000]
res_time = []
for n in n_list:
    matrix1 = np.zeros((n, n), dtype=int)
    matrix2 = np.zeros((n, n), dtype=int)
    for x in range(n):
        for y in range(n):
            matrix1[x][y] = random.randint(1, 50)
            matrix2[x][y] = random.randint(1, 50)
    time1 = time.time()
    strassen_mult(matrix1, matrix2)
    time2 = time.time()
    res_time.append(time2 - time1)
plt.plot(n_list, res_time)
plt.title("Strassen Matrices Multiplication")
plt.xlabel("matrix size")
plt.show()
