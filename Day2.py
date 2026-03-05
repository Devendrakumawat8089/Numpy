# Day2 of Numpy
import numpy as np

a = [1,2,3,4,5]
print(np.array(a))

# (3). eye() --> It Will Create an array in which digonal positional elements are 1 and rest all are 0.
a =np.eye(4)
print(a)
'''
[[1. 0. 0. 0.] 
 [0. 1. 0. 0.] 
 [0. 0. 1. 0.] 
 [0. 0. 0. 1.]]
 
'''
# (4). diag() --> it will set our custom values on digonal position \

a = np.array([1,45,78,90])
print(a) #[ 1 45 78 90]

b =np.diag(a)
print(b)
'''
[[ 1  0  0  0]
 [ 0 45  0  0]
 [ 0  0 78  0]
 [ 0  0  0 90]]
 
'''

# (5). Random Module 
# (a) Randint() --> it will create random numbers in a given range 
# Syntax :  np.random.randint(min_range , max_range , total_number)

a = np.random.randint(1,10,5)
print(a) # Output --> Rnadom 5 Number In range 1 to 10 

# (b) Rand() --> it will create random numbers in a range 0-1

a = np.random.rand(5)
print(a) #Random numbers in a range 0 to 1 

# (c). seed() --> it will fix our random generated data

np.random.seed(5)
a =np.random.randint(1,10,3)
print(a) # [4 7 7] (Fix The Random Generated number )

'''View Vs Copy'''
# View Means modification in original data and copy means changes in duplicate data will not reflect the original data 
a= np.array([10,20,30,40,50,60,70,80,])
print(a) #10 20 30 40 50 60 70 80]
print(a[3:6]) #[40 50 60]
print(a) #[10 20 30 40 50 60 70 80]

a= np.array([10,20,30,40,50,60,70,80,])
b= a[3:6] = 0
print(b)

a= np.array([10,20,30,40,50,60,70,80,])
b = a[3:6].copy()
b[:] = 0
print(b)
'''Operation on Arrary'''
# (1). arange() --> it will work as as for loop in numpy

a = np.arange(1,16)
print(a) #[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print(a>10) #[False False False False False False False False False False  True  True True  True  True]
b = a> 10 
print(a[b]) #[11 12 13 14 15]
b= a%2 == 0
print(a[b]) # it will retrun even number  --> [ 2  4  6  8 10 12 14]

'''Reshape Condition'''
# n(rows) * n(colums) =n(total_elemenets)

# total_elements =12 
# 1*12 , 2*6 , 6*2
# 3*4 , 4*3

a =np.random.randint(1,50,12)
print(a)

print(a.reshape(3,4))

a = np.arange(1,5).reshape(2,2)
print(a)
'''
[[1 2]
 [3 4]]
'''
b = np.arange(5,9).reshape(2,2)
print(b)
'''
[[5 6]
 [7 8]]
'''

print(a+b)
'''
[[ 6  8]
 [10 12]]
'''
print(a-b)

'''
[[-4 -4]
 [-4 -4]]
'''

print(a*b) 
'''
[[ 5 12]
 [21 32]]
 
 this is not Matrix Multiplaction 
'''
print(a.dot(b))
'''
[[19 22]
 [43 50]] 
 
 This is the matrix multaplaction
 '''
 
 