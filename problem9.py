import numpy as np
import sympy

def getvectorX(B,xB):
 # b1,b2,b3 = B
 # xb1,xb2,xb3 = xB
 res = []
 for i in range(len(B)):
  b = B[i]
  xb = xB[i]
  res.append(np.dot(b,xb))
 #get total sum
 r1,r2,r3 = 0,0,0
 for col in res:
  for index,val in enumerate(col):
   if index == 0:r1 +=val
   elif index == 1:r2 +=val
   elif index == 2:r3 +=val
 return [[r1],[r2],[r3]]



if __name__ == "__main__":
 B1 = np.array([[1],[-4],[3]])
 B2= np.array([[5],[2],[-2]])
 B3 = np.array([[4],[-7],[0]])

 xB = np.array([[3],[0],[1]])

 B = (B1,B2,B3)
 print(getvectorX(B,xB))
