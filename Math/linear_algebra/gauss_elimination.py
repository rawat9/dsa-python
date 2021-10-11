# A x = b
# 1. Elimination
# 2. Back Substitution

import numpy as np

A = np.array([[3,-2,5,0],
              [4,5,8,1],
              [1,1,2,1],
              [2,7,6,5]], float)

b = np.array([2,4,5,7], float)
n = len(b)

# Solution vector
x = np.zeros(n, float)

# 1. Elimination

for k in range(n-1): # to index fixed rows and cols
    for i in range(k+1,n):

        # if the element is already 0, skip to next i
        if A[i,k] == 0: 
            continue
        factor = A[k,k] / A[i,k]

        for j in range(k,n):
            A[i,j] = A[k,j] - A[i,j]*factor
            
        b[i] = b[k] - b[i]*factor


# 2. Back Substitution

# starting from last row
x[n-1] = b[n-1] / A[n-1, n-1]

for i in range(n-2,-1,-1):
    sum_ax = 0
    for j in range(i+1,n):
        sum_ax += A[i,j] * x[j]
    x[i] = (b[i] - sum_ax) / A[i,i]


print('The Solution of the system:')

for i in range(n):
    print('{}. {:.2f}'.format(i, x[i]))
