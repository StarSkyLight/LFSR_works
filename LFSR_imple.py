"""This file is for ii of question 3

It is the implementation of LFSR.
"""


def LFSR_imp():
    # This function is for the implementation of LFSR.

    # My exam number is Y3861906, so I use the number part of that.
    binary = get_binary('3861906')
    temp_ini_state = list(binary)
    # to get the initial statement
    state = temp_ini_state[len(binary)-15:]

    file = open("output.txt", "w")

    # calculate the 1000-bit output sequence
    for i in range(0, 1000):
        # get the last bit as the output and write it in a file
        output = state[len(state)-1]
        file.write(output)
        # get the result of XOR
        temp_xor = int(state[len(state)-1]) ^ int(state[0])
        temp_state = list(str(temp_xor))
        temp_state[1:] = state[0:len(state)-1]
        # refresh the statement
        state = temp_state

    file.close()


def get_binary(exam_num):
    # This function is for converting my exam number to binary.

    binary = ''

    # Every bit of the exam number is converted to a 4-bit binary.
    for i in range(0, len(exam_num)):
        temp = '{0:04b}'.format(int(exam_num[i]))
        binary = binary + temp

    return binary


LFSR_imp()
