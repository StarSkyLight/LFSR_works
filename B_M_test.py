def test():
    a = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    delta = [0]
    fail = [0]
    cnt = 0
    mul = 0
    r1 = [0]
    r = [0]

    delta[0] = 1
    fail[0] = 1
    cnt = 0
    r = [0]

    delta.append(1)
    fail.append(2)
    mul = 1
    cnt = 1
    r1[0] = 1
    r[0] = 1

    for i in range(3, len(a) + 1):
        temp_a = a[i-1]

        temp_delta = 0
        # for j in range(1, len(r) + 1):

