from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='ortho',
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

x, y = map(0, 0)
map.plot(x, y, marker='D',color='m')

lons = [1, 10, -20, -20]
lats = [1, -10, 40, -20]
x, y = map(lons, lats)
map.scatter(x, y, marker='D',color='m')

plt.show()