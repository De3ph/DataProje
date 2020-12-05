from math import sqrt #karekök fonksiyonu

class Banknot():

    varyans = None
    çarpıklık = None
    basıklık = None
    entropi = None
    gerçek = None

    #constructor metot
    def __init__(self ,varyans,çarpıklık,basıklık,entropi,gerçek=None):

        self.varyans = varyans
        self.çarpıklık = çarpıklık
        self.basıklık = basıklık
        self.entropi = entropi
        self.gerçek = gerçek

def KNN():
    
    varyans = float(input("varyans değeri : "))
    çarpıklık = float(input("çarpıklık değeri : "))
    basıklık = float(input("basıklık değeri : "))
    entropi = float(input("entropi değeri : "))

    k = int(input("k değeri : "))


    try:
        
        data_set_txt = open("data_banknote_authentication.txt")

        def seperate_rows(txt):

            data_rows = list()

            for i in txt.readlines():
                i = i.split(" ")
                i[0] = i[0].replace("\n" , "")
                i = i[0].split(",")
                data_rows.append(i)
            
            return data_rows
        
        data_rows = seperate_rows(data_set_txt)
        
        para = Banknot(varyans,çarpıklık,basıklık,entropi)

        def dist_list_maker(para , data_rows):

            dist_list = []

            for i in range(len(data_rows)):

                d = sqrt(
                    (float(data_rows[i][0]) - para.varyans)**2 + 
                    (float(data_rows[i][1]) - para.çarpıklık)**2 + 
                    (float(data_rows[i][2]) - para.basıklık)**2 + 
                    (float(data_rows[i][3]) - para.entropi)**2
                )

                isReal = data_rows[i][4]

                temp_tuple = tuple((d , isReal , i))
                
                dist_list.append(temp_tuple)
            
            dist_list.sort()

            return dist_list

        dist_list = dist_list_maker(para , data_rows)

        def classification(distList , k):

            isReal = 1

            k_list = distList[:k]

            real , fake = 0 , 0

            for i in range(len(k_list)):

                if k_list[i][1] == "1":
                    real +=1
                else:
                    fake += 1
                
            if int(real) > int(fake):
                isReal = 1
            else:
                isReal = 0
            
            print("*"*40)

            print("*"*40)

            return isReal , real , fake
            
        isReal , real , fake = classification(dist_list , k) 

        def print_classification(real , fake):
                print(real , " gerçek örnek, " , fake , " sahte örnek", "\n")
                
                if int(real) > int(fake):
                    print("Algoritmamızın tahminine göre banknot : Gerçek", "\n")
                else:
                    print("Algoritmamızın tahminine göre banknot : Sahte", "\n")
                    
        print_classification(real= real , fake= fake)

        def print_properties(dataRows , distList , k):

            for i in range(k):
                index = distList[i][2]
                print("Özellikleri : " , dataRows[index] , " uzaklığı : " ,distList[i][0] , "\n")

        print_properties(data_rows, dist_list , k)
        
        print("-"*50 , " Test Kısmı " , "-"*15)
        
        def success_rate():
            
            test_k = int(input("Test için k sayısı giriniz : "))

            success_guess = 0

            rate = 0

            test_data = open("test_verileri.txt")
            big_data = open("test_veri_1172.txt")

            test_data_rows = seperate_rows(test_data)
            big_data_rows = seperate_rows(big_data)

            for i in range(len(test_data_rows)):
                test_banknot = Banknot(

                    varyans= float(test_data_rows[i][0]),
                    çarpıklık= float(test_data_rows[i][1]),
                    basıklık= float(test_data_rows[i][2]),
                    entropi= float(test_data_rows[i][3]),
                    gerçek= float(test_data_rows[i][4])
                )

                test_dist_list = dist_list_maker(test_banknot , big_data_rows)

                isReal = classification(test_dist_list , test_k)

                if (int(test_banknot.gerçek) == int(isReal[0])):
                    success_guess += 1
                
                print(i+1 , ". paranın test sonucu : " , "\n", "Algoritma tahminine göre girilen banknotun türü : " , isReal[0] , " girilen banknotun asıl türü : " , int(test_banknot.gerçek))
                print("-"*25)

            rate = (success_guess / len(test_data_rows)) * 100

            print("Algoritmanın başarı oranı : " , format(rate , ".2f"), "%")

        success_rate()
    
        def print_dataset():
        
            show = input("Bellekteki veri setini görmek istiyorsanız 1'i tuşlayın :) ")

            if show == "1":
                for i in data_rows:
                    print(*i)

        print_dataset()

    except Exception as e:
        print("Hata", " " , e)
        
KNN()
input()