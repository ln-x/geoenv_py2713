import numpy as np
import matplotlib.pyplot as plt
"""
##1) add value
A = ([[1,1,1],[1,1,1],[1,1,1]])
mask = ([0,0,0],[0,1,0],[0,0,0])
mask2 = ([1,1,1],[1,0,1],[1,1,1])
A_ext = np.add(A,mask)
A_ext2 = np.add(A,mask2)
#A_ext = A.__add__(mask)
#A_ext =  A + mask
plt.imshow(A)
plt.show()
plt.imshow(A_ext)
plt.colorbar()
plt.show()
plt.imshow(A_ext2)
plt.colorbar()
plt.show()

##2) multiply value
mask3 = ([0.7,0.7,0.7],[0.7,0.4,0.7],[0.7,0.7,0.7])
A_ext3 = np.multiply(A,mask3)
plt.imshow(A_ext3)
plt.colorbar()
plt.show()

##3) replace value
arr = np.arange(6).reshape(2, 3)
print arr
arr[arr>2] = 2
print arr
arr[arr==2] = 5
print arr
"""
##4) find nearest neighbors and mark them
def n_closest(x,n,d=1):
    return x[n[0]-d:n[0]+d+1,n[1]-d:n[1]+d+1]

y = np.diag(np.ones(10))  #zero matrix with diagonal ones
#print np.diag(np.ones(10))
#print n_closest(y,(1,3)) #zweiter Array, viertes Element, default: radius 1
#print n_closest(y,(2,3),d=2) #dritter Array, viertes Element, radius 2

B = np.ones((10,10), dtype=np.int)
B[4,5] = 3
B[6,5] = 3
B[3,7] = 3
""""
B = ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
"""
#plt.imshow(B)
#plt.show()
print n_closest(B,(5,5),d=2)

exit()

