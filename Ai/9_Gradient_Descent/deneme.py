
with open("setam.txt","r") as dosya:
   sayı=1
   liste=[]
   asda=[]
   for satir in dosya:
        sayı+=1
        if sayı%2==0:
            liste.append(satir)
        else:
            pass
   for n in liste:
        n=str(n)
        n=n[:-1]
        asda.append(n)
   print(asda)