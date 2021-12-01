from numpy import linalg as LA
import numpy as np
import matplotlib.pyplot as plt
"""
Use np.linalg.eig to calculate the eigenvalues and eigenvectors of the given ma-
trix. Using matplotlib, plot the standard basis vectors, the vectors defined by the
columns of A, and the calculated eigenvectors. Save your script as problem8.py.
A =
[ 1 −2
 −4 1
] 
"""

def plot(eigenvalues,standard_basis_vector,vector_cols_A_1,vector_cols_A_2):
 fig, ax = plt.subplots()
 q = ax.quiver(eigenvalues, eigenvalues, vector_cols_A_1, vector_cols_A_2)
 ax.quiverkey(q, X=0.3, Y=1.1, U=5, label='Quiver key, length = 10', labelpos='E')
 plt.show()
 print(eigenvalues)
 print(standard_basis_vector)
 print(vector_cols_A_1)
 print(vector_cols_A_2)

def main():
 A = np.array([[1,-2], [-4,1]])
 res = LA.eig(A)
 eigenvalues, eigenvectors = res
 standard_basis_vector = np.identity(2) #standard basis vectors
 vector_cols_A_1 = A[:,0] #first column of A
 vector_cols_A_2 = A[:,1] #second column of A
 plot(eigenvalues,standard_basis_vector,vector_cols_A_1,vector_cols_A_2)
 return

if __name__ == '__main__':
 main()

