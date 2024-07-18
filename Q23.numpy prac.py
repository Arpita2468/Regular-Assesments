import numpy as np
arr = np.array([[0,1,2], [3,4,5]], dtype= np.float16)
arr
a = np.array([0,1])
b = np.array([9,8])
c = a
d = b.copy()
d[0] = 8
print(b)
print(d)
arr = np.arange(3,12)
print(repr(arr))
print(arr)
arr = np.linspace(5,11, num=4)
print(arr)
arr = np.arange(8)
reshaped_arr = np.reshape(arr[3:6], (1, 3))
print(reshaped_arr)