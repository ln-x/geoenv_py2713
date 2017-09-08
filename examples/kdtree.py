from scipy import spatial
import numpy as np
x, y = np.mgrid[0:5, 2:8]
tree = spatial.KDTree(list(zip(x.ravel(), y.ravel())))
print tree.data
pts = np.array([[0, 0], [2.1, 2.9]])
print tree.query(pts)
print tree.query(pts[0]) #(2.0, 0)