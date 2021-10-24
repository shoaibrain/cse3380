import numpy as np
import sympy

def getRREF(matrix):
 """
 returns rref of given numpy matrix
 """
 M = sympy.Matrix(matrix) #convert numpy array to sympy matrix class
 rref = M.rref()
 #convert sympy rref to numpy array
 A_rref = np.array(rref[0].tolist())
 return A_rref

def getColumnSpace(matrix):
 """
 returns the column space of matrix
 """
 M = sympy.Matrix(matrix) #convert numpy array to sympy matrix class
 col_space = M.columnspace()
 return col_space

def solveMatrixEquation(matrix,const):
 a = np.array(matrix)
 b = np.array(const)
 x = np.linalg.solve(a,b)
 return x

def getNullSpace(matrix):
 M = sympy.Matrix(matrix)#convert numpy array to sympy matrix class
 null_space = M.nullspace()
 return null_space


if __name__ == "__main__":
 #8.a:
 #convert numpy array to sympy.matrix class
 A = [[3,8,-5],[3,-6,-7],[3,4,2]]
 b = [-1,-1,3]
 A_rref = getRREF(A)
 print(f"Reduced echelon form of A is:\n{A_rref}\n")

 #8b. Find the column space of A
 A_column_space = getColumnSpace(A)
 print(f"Column space of A is:\n{A_column_space}")
 #8c. Solve the matrix equation Ax = b
 x = solveMatrixEquation(A,b)
 print(f"X =\n {x}")
 #8d. Compute Nul A
 A_nul = getNullSpace(A)
 print(f"Nullspace of A is:\n{A_nul}")