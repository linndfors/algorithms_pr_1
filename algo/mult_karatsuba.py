import time
import random
import matplotlib.pyplot as plt

def len_equality_change(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 < len2:
        for i in range(len2 - len1):
            str1 = '0' + str1
        return len2, str1, str2
    else:
        for i in range(len1 - len2):
            str2 = '0' + str2
    return len1, str1, str2


def bit_multiply(str1, str2):
    return int(str1[0]) * int(str2[0])


def store_bits(first, second):
    # To store the sum bits
    # make the lengths same before adding
    result = ""
    length, first, second = len_equality_change(first, second)
    helper = 0

    # Add all bits one by one
    for i in range(length):
        first_bit = int(first[length - 1 - i])
        second_bit = int(second[length - 1 - i])

        # boolean expression for sum of 3 bits
        sum = str((first_bit ^ second_bit ^ helper))

        result = str(sum + result)

        # boolean expression for 3-bit addition
        helper = (first_bit & second_bit) | (second_bit & helper) | (first_bit & helper)

    if helper:
        result = '1' + result
    return result


def kar_multiply_bin(numb1, numb2):
    n_size, numb1, numb2 = len_equality_change(numb1, numb2)
    if n_size == 0:
        return 0
    if n_size == 1:
        return bit_multiply(numb1, numb2)
    first_half = n_size // 2
    second_half = n_size - first_half

    left_part1 = numb1[0: first_half]
    right_part1 = numb1[first_half:]

    left_part2 = numb2[0: first_half]
    right_part2 = numb2[first_half:]
    part1 = kar_multiply_bin(left_part1, left_part2)
    part2 = kar_multiply_bin(right_part1, right_part2)
    part3 = kar_multiply_bin(store_bits(left_part1, right_part1), store_bits(left_part2, right_part2))

    # Combine the three products to get the final result
    res = part1 * (1 << (2 * second_half)) + (part3 - part1 - part2) * (1 << second_half) + part2
    return res

# time1 = time.time()
# bin_bit = [0, 1]
# number1 = ""
# number2 = ""
# for bit in range(5000):
#     number1 += str(random.choice(bin_bit))
#     number2 += str(random.choice(bin_bit))
# print(bin(kar_multiply_bin(number1, number2)))
# time2 = time.time()
# print(time2 - time1)


# bin_bit = [0, 1]
# number1 = ""
# number2 = ""
# sum = 0
# experiments = 10
# n = 10000
# for x in range(experiments):
#     number1 = ""
#     number2 = ""
#     for bit in range(n):
#         number1 += str(random.choice(bin_bit))
#         number2 += str(random.choice(bin_bit))
#     time1 = time.time()
#     kar_multiply_bin(number1, number2)
#     time2 = time.time()
#     my_time = time2 - time1
#     sum += my_time
# res_time = sum/experiments
# print("res time: ", res_time)
# f = open("karatsuba_multiplication.txt", "a")
# f.write(f"{n} ")
# my_time = "%.5f" % res_time
# f.write(str(my_time) + "\n")
# f.close()
# with open('karatsuba_multiplication.txt') as file:
#    df = file.read().splitlines()
#    # df = df.splitlines('\n')
# print(df)
# vert = []
# gor = []
# for row in df:
#     vert.append(float(row.split(" ")[0]))
#     gor.append(float(row.split(" ")[1]))
# plt.plot(vert, gor)
# plt.title("Karatsuba Multiplication")
# plt.xlabel("number's length")
# plt.show()
