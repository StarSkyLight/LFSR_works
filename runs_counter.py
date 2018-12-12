"""This file is for iv of Question 3.

This is a counter of the numbers of all lengths (1 to 10) of zero-ran and one-ran.
"""


def count_runs():
    file = open("output.txt", "r")

    # two lists to store the numbers of all lengths (1 to 10) of zero-ran and one-ran
    counter_zero_rans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter_one_rans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # This is the counter to count the number of zero-ran or one-ran in the loop
    counter = 1

    temp_last = file.read(1)
    # If it is the end of the file, stop the loop
    if temp_last == '':
        print(counter_zero_rans)
        print(counter_one_rans)
        return

    while True:
        # read a bit of the file
        temp = file.read(1)
        # If it is the end of the file, stop the loop and count the length of counted sequence
        if temp == '':
            # if the counted sequence is zero-run, add one to the counter of the corresponding length
            if int(temp_last) == 0:
                if 0 < counter <= 10:
                    counter_zero_rans[counter-1] = counter_zero_rans[counter-1] + 1
            # if the counted sequence is one-run, add one to the counter of the corresponding length
            elif int(temp_last) == 1:
                if 0 < counter <= 10:
                    counter_one_rans[counter-1] = counter_one_rans[counter-1] + 1
            break

        # if the counted sequence ends, calculate the length of it
        if int(temp) != int(temp_last):

            # if the counted sequence is zero-run, add one to the counter of the corresponding length
            if int(temp_last) == 0:
                if 0 < counter <= 10:
                    counter_zero_rans[counter-1] = counter_zero_rans[counter-1] + 1
            # if the counted sequence is one-run, add one to the counter of the corresponding length
            elif int(temp_last) == 1:
                if 0 < counter <= 10:
                    counter_one_rans[counter-1] = counter_one_rans[counter-1] + 1

            # refresh temp_last and counter
            temp_last = temp
            counter = 1
        # the sequence does not end, continue to count the length
        else:
            counter = counter + 1

    print(counter_zero_rans)
    print(counter_one_rans)

    file.close()


count_runs()
