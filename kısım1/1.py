import random

def Noktali_Uzay():
    
    Width = int(input("Width değeri : "))
    Height = int(input("Height değeri : "))
    Nokta_sayisi = int(input("Oluşturulacak nokta sayısı: "))

    def Bos_Uzay():
        uzay = []

        for i in range(Width):
            uzay.append([])
            for j in range(Height):
                uzay[i].append([])
        return uzay
    
    bos_uzay = Bos_Uzay()

    for i in range(Nokta_sayisi):
        x_point = random.randint(0,Width - 1)
        y_point = random.randint(0,Height - 1)
        bos_uzay[x_point][y_point] = [x_point , y_point]

    return bos_uzay

noktali_uzay = Noktali_Uzay()
