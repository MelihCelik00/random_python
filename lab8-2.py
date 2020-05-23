# -*- coding: utf-8 -*-
# author: Melih Safa Celik
# Student number: 010180519
# Bilinmesi gerekilen donusum formulu: (deg/360)=(radian/2pi)=(grad/400)

from math import pi #direkt import math da diyebilirsin

f_NO = open("gps_sites.txt","r")
readLines_NO = f_NO.readlines() 
# readlines() fonksiyonu ile tum satirları bir listede topluyor gibi dusunebiliriz
# Her bir satir bir eleman gibi oluyor asagida bunları ayiracagiz, split methodu ile
# Debug yapıp görmek istersen yorumu silip print ile test edebilirsin -> print(readLines_NO)

print("Station Name\t",
        "Latitude(deg)\t", "Longitude(deg)\t",
        "Latitude(grad)\t", "Longitude(grad)\t",
        "Latitude(radian)", "Longitude(radian)\t", sep="\t")



for oneLine_NO in readLines_NO:
    # Simdi oncelikle tum satirlardan 0. indexten baslayip son elemana yani satira kadar inceleyecegiz. 
    # For dongusune alma sebebimiz bu
    oneLine_NO = oneLine_NO.split()
    # Split methodu ile ilk satiri da ayrı ayrı elemanlara ayirdik. Ilk satırımızdaki elemanlari soyle dusunebiliriz
    # index:indexin ismi -> [0:Station Name, 1:X, 2:Y, 3:Z, 4:Latitude(deg), 5:Longitude(deg)]
    #####################
    # Simdi cevirmeleri yapalim, bu donusumler her for dongusunde bastan hesaplanacak ve direkt olarak basicaz.
    # Yani her satiri hesaplayacak ve ekrana basicak tek tek
    ### Gradlar
    latitudeDegreeToGrad_NO = float(oneLine_NO[4]) * 400 / 360
    longitudeDegreeToGrad_NO = float(oneLine_NO[5]) * 400 / 360
    ### Radianlar
    latitudeDegreeToRadian_NO = float(oneLine_NO[4]) * pi / 180
    longitudeDegreeToRadian_NO = float(oneLine_NO[5]) * pi / 180
    # Burada da tek tek tablar yapa yapa ayirarak, onceden buldugumuz ve hesapladigimiz degerleri basiyoruz terminale, bu da bize görsel hile yaparak bir tablo veriyor
    print("\n")
    print(format(oneLine_NO[0],"s"),"\t\t",end="\t")
    print(format(float(oneLine_NO[4]),".3f"),"\t\t",end="\t")
    print(format(float(oneLine_NO[5]),".3f"),"\t\t",end="\t")
    print(format(float(latitudeDegreeToGrad_NO),".3f"),"\t\t",end="\t")
    print(format(float(longitudeDegreeToGrad_NO),".3f"),"\t\t",end="\t")
    print(format(float(latitudeDegreeToRadian_NO),".3f"),"\t\t",end="\t")
    print(format(float(longitudeDegreeToRadian_NO),".3f"),"\t\t",end="\t")

print("\n") # Terminalde daha temiz bir goruntu olusturmak icin bir satir bosluk olsun
