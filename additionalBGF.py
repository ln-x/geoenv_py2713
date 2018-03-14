Tulln = 13.8
Korneuburg = 11.3
Klostern = 10.0
Moedling = 11.9
Schwechat = 19.1
Gaensernd = 15.9
Baden = 12.5
BruckL = 11.2
W01 = -3.0
W02 = 20.0
W03 = 14.5
W04 = 15.1
W05 = 16.0
W06 = 18.9
W07 = 16.7
W08 = 18.3
W09 = 17.9
W10 = 21.5
W11 = 17.6
W12 = 15.4
W13 = 3.3
W14 = 13.4
W15 = 19.5
W16 = 16.9
W17 = 15.0
W18 = 10.7
W19 = 8.3
W20 = 18.5
W21 = 22.1
W22 = 27.2

Wien2014=1766746
Wien2015=1794755
Wien2030=2077300
Wien2050=2286094

BH=20  #...tif      MAX: 17.7
Built=0.5  #...tif  MAX: 0.6
Geschoss=3
pixelsize=100 #10x10m
growthrate = 0. #oeROK xls (UmlandBezurek), MA23.csv (Wiener Bezirke)

if Built <0.8:
actualBGF = round(BH/Geschoss)*Built*pixelsize
newBGF = actualBGF*(growthrate+1)
newBuilt= newBGF/(round(BH/Geschoss)*pixelsize)
print actualBGF,newBGF, newBuilt




