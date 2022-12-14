szamok = []

def beker():
    szam1 = int(input("Adja meg a(z) 1. negatív egész számot: "))
    while szam1 >=0:
        szam1 = int(input("Adja meg újra a(z) 1. negatív egész számot: "))
    szamok.append(szam1)



    szam2 = int(input("Adja meg a(z) 2. negatív egész számot: "))
    while szam2 >=0:
        szam2 = int(input("Adja meg újra a(z) 2. negatív egész számot: "))
    szamok.append(szam2)

    szam3 = int(input("Adja meg a(z) 3. negatív egész számot: "))
    while szam3 >= 0:
        szam3 = int(input("Adja meg újra a(z) 2. negatív egész számot: "))
    szamok.append(szam3)


    legkisebb_negyzet = 0
    megadasi_sorrend = 0
    i = 0
    while i < len(szamok):
        if szam1 > szam2 and szam1 > szam3:
            legkisebb_negyzet = szam1
            megadasi_sorrend = i+1
        if szam2 > szam1 and szam2 > szam3:
            legkisebb_negyzet = szam2
            megadasi_sorrend = i + 1
        if szam3 > szam1 and szam3 > szam2:
            legkisebb_negyzet = szam3
            megadasi_sorrend = i + 1
    print(f"A legkisebb négyzetű szám: {legkisebb_negyzet}, megadási sorrendje: {megadasi_sorrend}")

beker()











