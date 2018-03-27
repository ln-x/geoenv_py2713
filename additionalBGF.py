#OEROK Prognosen 2014: until 2030, 2060
#Klostern = 10.0,21.7 -> + Tulln 13.8,28.1 -> 11.9, 24.9
#Schwechat = 19.1,39.6 -> Bruck an der Leitha 11.2, 22.7 -> 15.15, 31.15

Korneuburg = 11.3, 24.4
Moedling = 11.9, 24.3
Gaensernd = 13.3, 29.3
Baden = 12.1, 24.1
BruckL = 15.15, 31.15
Mistelbach = 4.7, 12.6
StPoeltenLand = 7.2, 13.9
KremsLand = 3.3,3.8
Tulln = 11.9, 24.9

W01 = -3.0,-2.7
W02 = 20.0,35.4
W03 = 14.5,26.1
W04 = 15.1,25.4
W05 = 16.0,29.4
W06 = 18.9,30.8
W07 = 16.7,27.2
W08 = 18.3,27.0
W09 = 17.9,29.7
W10 = 21.5,39.8
W11 = 17.6,34.2
W12 = 15.4,29.6
W13 = 3.3,8.7
W14 = 13.4,23.3
W15 = 19.5,33.8
W16 = 16.9,29.8
W17 = 15.0,25.9
W18 = 10.7,19.6
W19 = 8.3,16.8
W20 = 18.5,35.6
W21 = 22.1,44.9
W22 = 27.2,55.2
W23 = 14.5,29.2


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




