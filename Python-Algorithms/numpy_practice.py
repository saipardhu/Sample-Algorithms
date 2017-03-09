import numpy as np
a=np.array([[1,2,3,10],[4,5,6,11],[7,8,9,12]])
b = a[0:2,1:3]
print(b)
b[0,0]=77
