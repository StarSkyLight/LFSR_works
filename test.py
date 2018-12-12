import numpy.matlib
import numpy as np


def test():
    a = np.array([[1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 1],
               [1, 1, 0, 0]])

    b = np.array([[1],
                 [1],
                 [1],
                 [1]])

    e = np.array([1, 1, 1, 1])

    f = np.array([[1, 1, 0, 1, 0],
               [1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1],
               [1, 0, 0, 1, 0],
               [0, 0, 1, 0, 0]])

    g = np.array([0, 1, 0, 0, 0])

    c = np.array([0, 0, 0, 0])

    c[0] = 1

    d = np.array([2, 3, 4])

    c[1:4] = d

    a[0][0] = c[0]

    # print(np.linalg.solve(a, e))
    # print(np.matlib.zeros((15, 15)))
    temp = np.array(list('{0:015b}'.format(1)))
    print(d[0:1])


test()
