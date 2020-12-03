from math import sqrt

class Banknot():

    varyans = None
    çarpıklık = None
    basıklık = None
    entropi = None
    gerçek = None

    def __init__(self ,varyans,çarpıklık,basıklık,entropi):

        self.varyans = varyans
        self.çarpıklık = çarpıklık
        self.basıklık = basıklık
        self.entropi = entropi

def KNN():
    
    varyans = float(input("varyans değeri : "))
    çarpıklık = float(input("çarpıklık değeri : "))
    basıklık = float(input("basıklık değeri : "))
    entropi = float(input("entropi değeri : "))

    k = int(input("k değeri : "))


    try:
        data_set_txt = open("data_banknote_authentication.txt")

        data_rows = list()

        dist_list = list()

        for i in data_set_txt.readlines():
            i = i.split(" ")
            i[0] = i[0].replace("\n" , "")
            i = i[0].split(",")
            data_rows.append(i)
        
        para = Banknot(varyans,çarpıklık,basıklık,entropi)

        def dist_list_maker():

            dist_list = []

            for i in range(len(data_rows)):

                d = sqrt(
                    (float(data_rows[i][0]) - para.varyans)**2 + 
                    (float(data_rows[i][1]) - para.çarpıklık)**2 + 
                    (float(data_rows[i][2]) - para.basıklık)**2 + 
                    (float(data_rows[i][3]) - para.entropi)**2
                )

                isReal = data_rows[i][4]

                element = tuple((d , isReal))
                
                dist_list.append(element)
            
            dist_list.sort()

            return dist_list

        dist_list = dist_list_maker()

        def classification():
            k_list = dist_list[:k]

            real , fake = 0 , 0

            for i in range(len(k_list)):

                if k_list[i][1] == "1":
                    real +=1
                else:
                    fake += 1
            
            if int(real) > int(fake):
                print("Gerçek")
            else:
                print("Sahte")
            
            print(f"real {real} fake {fake}")

        classification()


    except Exception as e:
        print("Hata", " " , e)
        
KNN()