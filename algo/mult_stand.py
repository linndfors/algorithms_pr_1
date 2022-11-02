import time
import random
import matplotlib.pyplot as plt

def multiply_bin_stand(numb1, numb2):
    # number1 = bin(numb1)[2:][::-1]
    # number2 = bin(numb2)[2:][::-1]
    number1 = numb1[::-1]
    number2 = numb2[::-1]
    store = []
    for ind, x in enumerate(number2):
        store.append([0]*ind)
        for y in number1:
            store[ind].append(int(x)*int(y))
        store[ind] = store[ind][::-1]
    # store = store[::-1]
    result = []
    counter = 0
    max_length = len(store[-1])
    while counter < max_length:
        sum = 0
        for x in store:
            try:
                sum += x[-1 - counter]
            except IndexError:
                pass
        result.append(sum)
        counter += 1
    for ind, bit in enumerate(result):
        if bit != 0 and bit != 1:
            bin_bit = bin(bit)[2:][::-1]
            result[ind] = int(bin_bit[0])
            for i in range(1, len(bin_bit)):
                try:
                    result[ind + i] += int(bin_bit[i])
                except IndexError:
                    result.append(int(bin_bit[i]))
    bin_numb = "0b"
    for e in result[::-1]:
        bin_numb += str(e)
    # print(int(bin_numb, 2))


# # multiply_bin_stand(12, 40)
# bin_bit = [0, 1]
# # # ranges = [10, 100, 1000, 5000, 10000]
# number1 = ""
# number2 = ""
# sum = 0
# experiments = 10
# n = 3000
# for x in range(experiments):
#     number1 = ""
#     number2 = ""
#     for bit in range(n):
#         number1 += str(random.choice(bin_bit))
#         number2 += str(random.choice(bin_bit))
#     time1 = time.time()
#     multiply_bin_stand(number1, number2)
#     time2 = time.time()
#     my_time = time2 - time1
#     sum += my_time
# res_time = sum/experiments
# print("res time: ", res_time)
# f = open("standard_multiplication.txt", "a")
# f.write(f"{n} ")
# my_time = "%.5f" % res_time
# f.write(str(my_time) + "\n")
# f.close()
with open('standard_multiplication.txt') as file:
   df = file.read().splitlines()
   # df = df.splitlines('\n')
# print(df)
vert = []
gor = []
for row in df:
    vert.append(float(row.split(" ")[0]))
    gor.append(float(row.split(" ")[1]))
# print(gor)
# print(vert)
plt.plot(vert, gor)
plt.title("Standart Multiplication")
plt.ylabel("time")
plt.xlabel("number's length")
plt.show()
