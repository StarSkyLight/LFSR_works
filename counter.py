"""This file is for iii of Question 3.

This is a counter of ones and zeros.
"""


def count():
    # This function is for counting ones and zeros in tht output sequence

    file = open("output.txt", "r")

    counter_zero = 0
    counter_one = 0
    # read every bit of the file and count
    while True:
        # read a bit of the file
        temp = file.read(1)
        # If it is the end of the file, stop the loop
        if temp == '':
            break
        # assess the bit and count it for one or zero
        if int(temp) == 0:
            counter_zero = counter_zero + 1
        elif int(temp) == 1:
            counter_one = counter_one + 1
    print('number of zeros is ' + str(counter_zero))
    print('number of ones is ' + str(counter_one))


count()
