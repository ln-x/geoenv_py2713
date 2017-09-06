import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(9.0).reshape((3, 3))
print x1
x2 = np.arange(3.0)
print np.add(x1, x2)
A = ([[1,1,1],[1,1,1],[1,1,1]])
mask = ([0,0,0],[0,1,0],[0,0,0])
mask2 = ([1,1,1],[1,0,1],[1,1,1])
mask3 = ([0.7,0.7,0.7],[0.7,0.4,0.7],[0.7,0.7,0.7])
A_ext = np.add(A,mask)  #add value
A_ext2 = np.add(A,mask2)
A_ext3 = np.multiply(A,mask3) #multiply value
#A_ext4 = np.place(A, A>0.5, 5) #replace value


arr = np.arange(6).reshape(2, 3)
print arr
arr[arr>2] = 2
print arr

arr[arr==2] = 5
print arr

#plt.colorbar()
#plt.imshow(arr)
#plt.show()

exit()

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
plt.imshow(A_ext3)
plt.colorbar()
plt.show()
#plt.imshow(A_ext4)
#plt.colorbar()
#plt.show()