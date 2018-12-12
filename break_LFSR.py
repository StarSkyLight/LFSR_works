"""This file is for ii of question 3

It is for breaking the LFSR and getting the initial statement of the LFSR
"""

import numpy as np


def breaker():
    # this function is for breaking the LFSR
    # this function try to solve the equation of the statements to break the LFSR

    file = open("output.txt", "r")

    # locate the 500th bit
    file.seek(499)

    # initialize a 15 * 15 array
    statements = np.zeros((15, 15), dtype=int)

    # read file to fill the array from the 500th bit
    for n in range(0, 15):
        statements[0][n] = int(file.read(1))

    for i in range(0, 14):
        last_row = statements[i]
        new_bit = int(file.read(1))
        temp_array = np.zeros(15, dtype=int)

        temp_array[0:14] = last_row[1:15]
        temp_array[14] = new_bit

        statements[i+1] = temp_array

    # this is the 16th statement of the sequence
    last_state = np.zeros(15, dtype=int)
    last_state[0:14] = statements[14][1:15]
    last_state[14] = int(file.read(1))

    # initialize an array to try all the possibilities
    test = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    # 2^15 is 32768
    # try all the 2^15 possibilities
    for m in range(0, 32768):
        # transfer the number to 15-length binary
        temp = list('{0:015b}'.format(m))
        test_str = np.array(temp)

        # transfer the binary from string to int and put it into test
        for k in range(0, 15):
            test[k] = int(test_str[k])

        # this is the result of multiplication of two arrays (test and statements)
        result = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # calculate the multiplication
        for p in range(0, 15):
            # get a row from statements
            temp_statements = statements[p]

            temp_product = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            # calculate the multiplication for every bit and put the result in temp_product
            for q in range(0, 15):
                temp_product[q] = temp_statements[q] * test[q]

            # get the result of XOR for ever bit
            temp_xor = temp_product[0] ^ temp_product[1]
            for g in range(2, 15):
                temp_xor = temp_xor ^ temp_product[g]

            # put the XOR result in result
            result[p] = temp_xor

        # use the function, is_same(), to assess if the result of calculation is same with the known result (last_state)
        if is_same(last_state, result):
            # if the two results are same, print the solution (test)
            print(polynomial(test))
            # use the solution to calculate the initial statement with function first_state()
            first_state(500, statements[0])

    file.close()


def is_same(last_state, result):
    # this function is for assessing if the two arrays is same

    same = True
    # assess if the result of XOR of every corresponding bit of them
    # result of XOR is 1 means they are different
    for i in range(0, 15):
        if (last_state[i] ^ result[i]) != 0:
            same = False
            break

    return same


def polynomial(taps):
    # this function transfer array to polynomial form
    plo = ''
    for i in range(0, 15):
        if taps[i] == 1:
            plo = plo + '+' + 'x^' + str(i+1)

    return '1' + plo


def first_state(bit_num, state):
    # this function is for getting the initial statement of the LFSR
    first_stat = state
    for i in range(0, bit_num - 1):
        temp = int(first_stat[14]) ^ int(first_stat[13])
        temp_stat = list(str(temp))
        temp_stat[1:] = first_stat[0:14]
        first_stat = temp_stat
    print(first_stat)


breaker()
