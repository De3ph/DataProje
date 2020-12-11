from math import sqrt #karekök fonksiyonu

class Banknot():

    varyans = None
    çarpıklık = None
    basıklık = None
    entropi = None
    gerçek = None

    # Banknot sınıfı için constructor metot
    def __init__(self ,varyans,çarpıklık,basıklık,entropi,gerçek=None):

        # self, Java dilindeki this deyiminin Python karşılığı
        self.varyans = varyans
        self.çarpıklık = çarpıklık
        self.basıklık = basıklık
        self.entropi = entropi
        self.gerçek = gerçek

def KNN():
    
    '''
    kodun try-catch bloğu içinde yazılmasının sebepi, ortaya çıkabilecek hataların konsolda yazdırılmasıdır.
    '''

    try:
        
        def seperate_rows(txt):
            # verisetinin her bir satırını daha kolay kullanmak için ayrıştırıp data_rows isimli listeye atadık.

            data_rows = list()

            for i in txt.readlines():
                i = i.split(" ")
                '''
                en sonda bulunan '\n' kaçış dizisi dosyalarda yazılmadığı için veriler, '\n' kadar alındı (satır sonuna kadar)
                split metodu verilen parametrelere kadar objeyi elemanlarına ayırır ve her birini string türünde bir eleman olacak şekilde bir liste döndürür
                '''
                i[0] = i[0].replace("\n" , "") # Verilen verisetindeki her bir satırın sonunda alt satıra geçiren '\n' kaçış dizisi bulunduğu için, değerleri alırken hata çıkmaması için kaldırıldı.
                i = i[0].split(",") # her bir satırdaki veriler "," lerden ayırıp tekrar listeye ekledi
                data_rows.append(i) # veri setinin i. satırı listeye atandı
            
            return data_rows
            

        def dist_list_maker(para , data_rows):

            dist_list = [] # İnput ile Baknot örneği olan para ile verisetindeki örnek paralarla aralarındaki uzaklığı tutacak liste.

            for i in range(len(data_rows)):

                #uzaklığı verilen formüle göre hesaplıyoruz.
            
                d = sqrt(
                    (float(data_rows[i][0]) - para.varyans)**2 + 
                    (float(data_rows[i][1]) - para.çarpıklık)**2 + 
                    (float(data_rows[i][2]) - para.basıklık)**2 + 
                    (float(data_rows[i][3]) - para.entropi)**2
                )
                
                isReal = data_rows[i][4] # verisetindeki örnek paraların türünü isReal değişkeninde depoluyoruz.

                temp_tuple = tuple((d , isReal , i)) # uzaklığı , türünü , satır indexini geçici olarak bir demette depolayarak sonrasında uzaklık tutan dist_list e ekliyoruz.
                
                dist_list.append(temp_tuple)
            
            dist_list.sort() # dist_list listesini d ye göre artan biçimde sort metodu ile sıralıyoruz, tuttuğumuz index ile kaçıncı satırda olduğunu kaybetmiyoruz.

            return dist_list


        def classification(distList , k):

            # KNN algoritması ile paranın türünün tahmin edilmesi için sınıflandırma fonksiyonu.

            isReal = 1 # gerçek ve sahte örneklerin sayısını hesaplamak için geçici olarak 1 değeri atandı. 

            k_list = distList[:k] # dist listi girilen k değerine kadar dist_list ten k_list adlı listeye değişkenleri kopyalıyor

            real , fake = 0 , 0

            for i in range(len(k_list)):

                if k_list[i][1] == "1": 
                    real +=1
                else:
                    fake += 1

            # oy çoğunluğuna göre paranın türü atanıyor  

            if real > fake:
                isReal = 1
            elif real < fake:
                isReal = 0
            else:
                isReal = int(dist_list[0][1])

            print(" ")

            return isReal , real , fake
            

        def print_classification(real , fake):

                print(real , " gerçek örnek, " , fake , " sahte örnek", "\n")
                
                if int(real) > int(fake):
                    print("Algoritmamızın tahminine göre banknot : Gerçek", "\n")
                else:
                    print("Algoritmamızın tahminine göre banknot : Sahte", "\n")
                    

        def print_properties(dataRows , distList , k):
            
            print("Varyans","Çarpıklık","Basıklık","Entropi","Tür","Uzaklık" , sep=" "*7)
            print("-"*70)

            for i in range(k):
                index = distList[i][2] #index değişkeni, yakın örneğin veri setindeki satır değişkenini tutuyor
                print("-" * 70)
                print(*data_rows[index] , sep=" "*8,end=" "*10) #en başa bırakılan yıldız liste elemanı yazdırırkenki elemanın parantezlerini ve virgüllerini kaldırıyor
                print(dist_list[i][0])
        

        def success_rate():
            
            test_k = int(input("Test için k sayısı giriniz : "))

            success_guess = 0

            rate = 0

            test_data = open("test_verileri.txt")
            big_data = open("test_veri_1172.txt")

            # yukarda tanımladığımız fonksiyonları başarı ölçümü kısmında tekrar kullandık

            test_data_rows = seperate_rows(test_data)
            big_data_rows = seperate_rows(big_data)

            for i in range(len(test_data_rows)):
                # data_banknote_authentication dosyasından alınan örnekleri Banknot örneği olarak oluşturuyor (karşılaştırma için)

                test_banknot = Banknot(

                    varyans= float(test_data_rows[i][0]),
                    çarpıklık= float(test_data_rows[i][1]),
                    basıklık= float(test_data_rows[i][2]),
                    entropi= float(test_data_rows[i][3]),
                    gerçek= float(test_data_rows[i][4])
                )

                test_dist_list = dist_list_maker(test_banknot , big_data_rows) # test verileri için dist list oluşturuyor.

                isReal = classification(test_dist_list , test_k) # paranın türünü classification fonksiyonunu kullanarak tahmin edip isReal değişkenine atıyor

                if (int(test_banknot.gerçek) == int(isReal[0])): # tahmin ile gerçek türünü karşılaştırıyor. classification sınıfı 3 adet değişkeni tuple(demet) içinde döndürdüğünden sadece tür bilgisini [0] ile alıyoruz
                    success_guess += 1
                
                def print_test_properties(test_data_rows, test_dist_list , test_k):
                    
                    print("Varyans","Çarpıklık","Basıklık","Entropi","Tür","Uzaklık" , sep=" "*7)
                    print("-"*70)

                    i = 0
                    while i != test_k:
                        index = test_dist_list[i][2]
                        print("-" * 70)
                        print(*big_data_rows[index] , sep=" "*8,end=" "*10)
                        print(test_dist_list[i][0])

                        i += 1

                    print("Bu paranın test sonucu : " , "\n", "Algoritma tahminine göre girilen banknotun türü : " , isReal[0] , " girilen banknotun asıl türü : " , int(test_banknot.gerçek))
                    print("*" *100)

                print_test_properties(test_data_rows , test_dist_list , test_k)
                
            rate = (success_guess / len(test_data_rows)) * 100

            print("Algoritmanın başarı oranı : " , format(rate , ".2f"), "%") #format ile düzgün yazdırılıyor

    
        def print_dataset():
        
            show = input("Bellekteki veri setini görmek istiyorsanız 1'i tuşlayın... ")

            if show == "1":
                for i in data_rows:
                    print(*i)
        
        #-------------------------------- Program çalıştırıldı ------------------------------------#
        
        varyans = float(input("varyans değeri : "))
        çarpıklık = float(input("çarpıklık değeri : "))
        basıklık = float(input("basıklık değeri : "))
        entropi = float(input("entropi değeri : "))

        k = int(input("k değeri : "))
       
        data_set_txt = open("data_banknote_authentication.txt")

        data_rows = seperate_rows(data_set_txt)

        para = Banknot(varyans,çarpıklık,basıklık,entropi)

        dist_list = dist_list_maker(para , data_rows)
        
        isReal , real , fake = classification(dist_list , k) 

        print_classification(real= real , fake= fake)

        print_properties(data_rows, dist_list , k)

        print(" ")
        print(" ")

        print("-"*50 , " Test Kısmı " , "-"*15)
        print(" ")
        success_rate()

        print_dataset()

    except Exception as e:
        print("Hata", " " , e)
        
KNN()
