# I have used numpy to compute the eigen values and eigen vectors of a given squre matrix

import numpy as np

size = int(input('Enter the size of the square array : '))
mat = []

print('Enter elements row wise : ')

for i in range(0, size):
    tmp = [int(x) for x in input().split()] 
    mat.append(tmp)

# find the eigen value and eigen vectors of this given array
w, v = np.linalg.eig(mat)
# w = eigen values, v = eigen vectors

print('Eigen values of given array : ', w)
print('Eigen vectors of given array : \n', v)