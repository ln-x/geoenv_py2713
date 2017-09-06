import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#A = np.array([[1,2],[3,4]])
#print A
#plt.imshow(A)

img=mpimg.imread('CORINE_2006_g100_06_Wien.png')
plt.imshow(img)
#plt.colorbar()
plt.show()

plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()

