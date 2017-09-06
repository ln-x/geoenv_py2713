__author__ = 'lnx'
import numpy as np
import matplotlib.pyplot as plt
import gdal
import sys
gdal.UseExceptions() # this allows GDAL to throw Python Exceptions
import scipy
#import random

#GEOPLAYGROUND
input_file = "D:/_URBANIA/GEODATA/DOM/2_raw/singletiles/raster/15_2_DOM.tif"
src_ds = gdal.Open( input_file )
cols = src_ds.RasterXSize
rows = src_ds.RasterYSize
bands = src_ds.RasterCount
driver = src_ds.GetDriver().LongName
geotransform = src_ds.GetGeoTransform()
print cols, rows, bands, driver, geotransform

exit()

def Usage():
    print("""
    $ getrasterband.py [ band number ] input-raster
    """)
    sys.exit(1)

def main( band_num, input_file ):
    src_ds = gdal.Open( input_file )
    if src_ds is None:
        print 'Unable to open %s' % input_file
        sys.exit(1)

    try:
        srcband = src_ds.GetRasterBand(band_num)
    except RuntimeError, e:
        print 'No band %i found' % band_num
        print e
        sys.exit(1)


    print "[ NO DATA VALUE ] = ", srcband.GetNoDataValue()
    print "[ MIN ] = ", srcband.GetMinimum()
    print "[ MAX ] = ", srcband.GetMaximum()
    print "[ SCALE ] = ", srcband.GetScale()
    print "[ UNIT TYPE ] = ", srcband.GetUnitType()
    ctable = srcband.GetColorTable()

    if ctable is None:
        print 'No ColorTable found'
        sys.exit(1)

    print "[ COLOR TABLE COUNT ] = ", ctable.GetCount()
    for i in range( 0, ctable.GetCount() ):
        entry = ctable.GetColorEntry( i )
        if not entry:
            continue
        print "[ COLOR ENTRY RGB ] = ", ctable.GetColorEntryAsRGB( i, entry )

if __name__ == '__main__':

    if len( sys.argv ) < 3:
        print """
        [ ERROR ] you must supply at least two arguments:
        1) the band number to retrieve and 2) input raster
        """
        Usage()

    main( int(sys.argv[1]), sys.argv[2] )


exit()