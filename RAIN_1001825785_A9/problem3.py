"""
3. Compute the QR factorization of the given matrix A using scipy.linalg.qr. Verify
R by hand using the Q matrix that was computed. Save your script as problem3.py.
A =
[ 1 0 4
 −2 3 −2
 −2 0 6
] 
"""

import numpy as np
  

def getDecom():
 # Original matrix
 matrix1 = np.array([[1,0,4], [-2,3,-2],[-2,0,6]])
 print(matrix1)
 # Decomposition of the said matrix
 q, r = np.linalg.qr(matrix1)
 print('\nQ:\n', q)
 print('\nR:\n', r)


if __name__ == '__main__':
 getDecom()