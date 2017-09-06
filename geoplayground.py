__author__ = 'lnx'
import numpy as np
import gdal
import sys
import matplotlib.pyplot as plt
gdal.UseExceptions() # this allows GDAL to throw Python Exceptions

#GEOPLAYGROUND
input_file = "D:/_URBANIA/GEODATA/DOM/2_raw/singletiles/raster/15_2_DOM.tif"
src_ds = gdal.Open( input_file )
driver = src_ds.GetDriver().LongName
geotransform = src_ds.GetGeoTransform()
    #geotransform[0] - originX - top left x
    #geotransform[1] - WE pixelWidth - w-e pixel resolution
    #geotransform[2] - rotation, 0 if image is "north up"
    #geotransform[3] - originY - top left y
    #geotransform[4] - rotation, 0 if image is "north up" */
    #geotransform[5] - NS pixelWidth - n-s pixel resolution
print driver, geotransform
print "[ METADATA ] = ", src_ds.GetMetadata()
print "[ COLS ] = ", src_ds.RasterXSize
print "[ ROWS ] = ", src_ds.RasterYSize
print "[ BANDNR. ] = ",src_ds.RasterCount
band = src_ds.GetRasterBand(1)
bandtype = gdal.GetDataTypeName(band.DataType)
scanline = band.ReadRaster( 0, 0, band.XSize, 1,band.XSize, 1, band.DataType)
print bandtype, scanline
print "[ MIN ] = ", band.GetNoDataValue()
print "[ MIN ] = ", band.GetMinimum()
print "[ MAX ] = ", band.GetMaximum()
print "[ SCALE ] = ", band.GetScale()
print "[ UNIT TYPE ] = ", band.GetUnitType()
#ctable = band.GetColorTable()
#if ctable is None:
#    print 'No ColorTable found'
#    sys.exit(1)
#print "[ COLOR TABLE COUNT ] = ", ctable.GetCount()
#for i in range(0, ctable.GetCount()):
#    entry = ctable.GetColorEntry(i)
#    if not entry:
#        continue
#    print "[ COLOR ENTRY RGB ] = ", ctable.GetColorEntryAsRGB(i, entry)
src_ds_array = src_ds.ReadAsArray()
print src_ds_array

#plt.hist2d(lc[0],lc[1])
plt.imshow(src_ds_array,interpolation='nearest', vmin=0 )#, cmap=plt.cm.gist_earth)
plt.colorbar()
plt.show()





#src_ds = None #delete raster to save space
