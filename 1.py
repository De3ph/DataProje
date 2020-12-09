from random import uniform
from math import sqrt

'''
ilk satır random float sayı üretmek için , ikinci satır karekök fonksiyonu almak için import edildi.
'''

def twoDVector():
    
    Width = float(input("Width değeri : "))
    Height = float(input("Height değeri : "))
    Nokta_sayisi = int(input("Oluşturulacak nokta sayısı: "))

    def nokta_uret(Nokta_sayisi):
        '''
        
        nx2 lik boş matris oluşturuldu
        random üretilen noktanın x ve y koordinatı üretilip geçici bir eleman adlı listede depolandı, böylelikle ileride x ve y değerlerine erişim daha kolaylaştırıldı.
        eleman listesine koordinatlar x,y sırasıyla eklenildi ve sonrasında nx2 lik matrise eklendi.

        '''
        nx2 = [] 
        

        for i in range(Nokta_sayisi):
            x_point = uniform(0,Width)
            y_point = uniform(0,Height)
            eleman = []
            eleman.append(x_point)
            eleman.append(y_point)
            nx2.append(eleman)
        
        return nx2


    nx2 = nokta_uret(Nokta_sayisi) # İstenilen nokta sayısı kadar nokta 2D uzayda üretilip matrise atandı.

    nxn = [] # Distance matris oluşturuldu

    for i in range(len(nx2)): # len fonksiyonu uzaklığı döndürüyor
        nxn.append([]) # her ilk for döngüsünde nxn matris için satır oluşturuluyor.

        for j in range(len(nx2)):

            dist_list = [] # uzaklıkların tutulduğu bir liste oluşturuluyor. 
            d = format(sqrt((nx2[i][0] - nx2[j][0])**2 + (nx2[i][1] - nx2[j][1])**2) , ".2f") # her bir noktanın diğer noktalara olan uzaklığı hesaplanıyor.
            dist_list.append(d)
            nxn[i].append(dist_list) # nxn matrisinin i. satırına uzaklıklar ekleniyor

    

    def print_style():
        
        '''
        nxn olan distance matrisini daha okunaklı yazdırmak için bir metot
        '''

        print("-"*10*Nokta_sayisi)

        print("  " , end= "  ")

        for i in range(len(nxn)):
            if i != len(nxn) - 1:
                print(" " * 7 , i , end=" ")
            else:
                print(" " * 7, i)

        print("-"*10*Nokta_sayisi)

        for i in range(len(nxn)):
            print(" | ", i , end="  | ")
            print(*nxn[i]) # en baştaki yıldız, print esnasında listedeki elemanları izole ederek yazdırıyor ( dıştaki büyük listenin parantezi ile aradaki virgülleri yok ediyor, kaldırılması program akışını etkilemiyor)
            print("-"*10*Nokta_sayisi)

    print_style()


twoDVector() # genel metot çalıştırılıyor.
