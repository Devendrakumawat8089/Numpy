# Day1  of Numby
# numpy --> Numerical Python (Mathematical calculations)
# Array --> Similar Data Types Collectionm

import numpy as np #First Import NumPy Short Name is np 


l = [1,2,3,4,5] # List is Comma(,) Seprated 
a=np.array(l)
print(a) # Arrary Is  Space Seprated -->  [1 2 3 4 5]

list1 =[1,2,3,4]
list2 = [4,5,6,7]
b = np.array([list1,list2])
print(b) 
'''
[[1 2 3 4] 
 [4 5 6 7]]
'''
# .ndim --> returns The Dimensions (1d , 2d ,3d)
print(b.ndim) # 2 

print(b.shape) #(2, 4) --> 
print(b.size) # 8 --> It Will Return THe Total Number Of Elements

a = np.ones(3)
print(a) #[1. 1. 1.]

a = np.zeros(3)
print(a) #[0. 0. 0.]

print(a.dtype) # float64