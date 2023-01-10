# Hozzunk létre egy metódust, mely törli a képernyőt (bármely OS esetén)!


# A testadatok.txt fájlt olvassátok be egy szótár adatszerkezetbe,
# kulcsok, azaz: oszlopnevek: nev, testmag, testsuly legyenek,
# használjátok az osztaly és a diak változóneveket
# enkódolást ne erőltessétek
# az elválasztó karaterre figyeljetek
# az 1. sornál figyeljetek arra, h nem adatokat tartalmaz (utólag is törölhető...)


# irassátok ki az osztáy tanulóinak csak a nevét az Osztálynvésor alá


# hozzatok létre egy osztaly_nevsor listát a nevekből
# rendezetten írassátok ki a neveket


# Írassátok ki azon diákok nevét, akik az átlag testmagasság alatt vannak!






#torles
import os
import platform

def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    

torles()


# fajl be


if os.path.exists('E:\\info-erettsegi felkeszito\\python komplex\\testadatok.txt'):
    testadatok = open('E:\\info-erettsegi felkeszito\\python komplex\\testadatok.txt', 'r')
else:
    print('nem talalom a fajlt')

#deklaráljuk a listakat és a szotart

ember_adatok = {}
nevek = []
magassagok = []
testtomegek = []

#split, de az elso sor is benne van

for sor in testadatok:
    testadatai = sor.split()
    nevek.append(testadatai[0])
    magassagok.append(testadatai[1])
    testtomegek.append(testadatai[2])


# kivesszuk a listakbol az oszlop elso elemet


nevek.pop(0)
magassagok.pop(0)
testtomegek.pop(0)

#tanulo nevek kiiratasa 

print("Osztalynevsor\n")
print(*nevek)

#rendezve
nevek.sort()
print()
print(*nevek)

#átlag megh.


int_magassagok = []
for magassag in magassagok:
    int_magassagok.append(int(magassag))

atl_cikl = 0
ossz_magassag = 0

while atl_cikl < len(magassagok):
    ossz_magassag = ossz_magassag + int_magassagok[atl_cikl]
    atl_cikl += 1

atlag = ossz_magassag/len(magassagok)

#megkeressuk kik vannak ez alatt
#csak tanarno kedveert most az egyszer for-al :)


atlag_alattiak = []



for magassag in int_magassagok:
    if magassag < atlag:
        atlag_alattiak.append(nevek[int_magassagok.index(magassag)])

#kiiratas

print("\nAz atlag alattiak neve:")
print(*atlag_alattiak)
