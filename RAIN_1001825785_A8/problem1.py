import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

# Cosine similarity measures the similarity between two non-zero vectors using the
# dot product
#returns cosine similarity scores
def _cosine_similarity(input_mat):
 #change input to np.array
 A_sparse = sparse.csr_matrix(input_mat)
 # pairwise dense output
 similarities = cosine_similarity(A_sparse)
 return similarities


# (b) Generate a random M ×N matrix and use it as input to your function to test
#returns a random mxn matrix with values ranging from int 0 - 20
def _get_random_mxn_matrix(m,n):
 return np.random.randint(0, high=20, size=(m,n), dtype='l')

# (c) Create a matplotlib plot and use the matshow function to display the scores.
def _create_plot():
 pass

if __name__ == '__main__':
 a = _get_random_mxn_matrix(3,4) #numpy.ndarray
 print(a)
 similarities = cosine_similarity(a)
 print(similarities)