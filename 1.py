from random import uniform
from math import sqrt
    

def twoDVector():
    Width = float(input("Width değeri : "))
    Height = float(input("Height değeri : "))
    Nokta_sayisi = int(input("Oluşturulacak nokta sayısı: "))

    def nokta_uret(Nokta_sayisi):
        nx2 = []
        for i in range(Nokta_sayisi):
            x_point = uniform(0,Width)
            y_point = uniform(0,Height)
            eleman = []
            eleman.append(x_point)
            eleman.append(y_point)
            nx2.append(eleman)
        
        return nx2
            
    nx2 = nokta_uret(Nokta_sayisi)

    nxn = []

    for i in range(len(nx2)):
        nxn.append([])

        for j in range(len(nx2)):
            dist_list = []
            d = format(sqrt((nx2[i][0] - nx2[j][0])**2 + (nx2[i][1] - nx2[j][1])**2) , ".3f")
            dist_list.append(d)
            nxn[i].append(dist_list)

    i = 0

    while(i < len(nxn)):
        print(nxn[i])
        i +=1

twoDVector()
