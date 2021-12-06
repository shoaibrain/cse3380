"""
1. There are multiple ways to compute eigenvectors. To familiarize yourself with the
relationship between eigenvalues and singular values, explore the outcomes of both
using numpy.
(a) Create a Python program that generates a random N ×M matrix X.
(b) Next, compute the eigendecomposition of the covariance matrix XT X using
numpy.linalg.eig.
(c) Project the computed eigenvectors onto the data via matrix multiplication and
normalize them so that the vectors are of length 1.
(d) Using numpy.linalg.svd(X, full_matrices=False), compute the singular
value decomposition of the matrix X.
(e) Compare the U matrix produced by numpy.linalg.svd and the normalized
eigenvectors computed in step 3. Write down any similarities or interesting
observations as a comment in your program file.

"""
import numpy as np

# get a random MXN matrix with int values in range (0,20) inclusive
def generate_random_NXM_matrix(M,N):
 return np.random.randint(0, 20+1, (M,N))

#b.
def compute_eigendecomposition(X):
 X_transpose = np.transpose(X)
 

#c.
def project_eigenvectors():
 pass

#d.
def singular_value_decomposition():
 pass

def main():
 X = generate_random_NXM_matrix(3,2)
 print(X)

if __name__ == '__main__':
 main()