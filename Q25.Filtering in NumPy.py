import numpy as np
print(repr(np.where([True, False, True])))
arr = np.array([0, 3, 5, 3, 1])
print(repr(np.where(arr == 3)))
arr = np.array([[0, 2, 3],
                [1, 0, 0],
                [-3, 0, 0]])
x_ind, y_ind = np.where(arr != 0)
print(repr(x_ind)) 
print(repr(y_ind)) 
print(repr(arr[x_ind, y_ind]))