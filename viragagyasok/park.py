import os, platform
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


if os.path.exists('forras.txt'):
    fajl = open('forras.txt', 'r')
else:
    print('nem talalom a fajlt')


forras = []
elso = []
utolso = []
szinek = []
viragagyasok = 0

for sor in fajl:
    forras.append(sor)

for sor in forras:
    if sor == forras[0]:
        viragagyasok = int(forras[0])
    else:
        agyasok_adatai = sor.split()
        elso.append(int(agyasok_adatai[0]))
        utolso.append(int(agyasok_adatai[1]))
        szinek.append(agyasok_adatai[2])


'''
2.feladat
Írja ki, hány felajánlást tartalmaz az állomány!
''' 

print('2.feladat')
print(f'A felajanlasok szama: {len(szinek)}\n')

'''
3.feladat
Jelenítse meg a képernyőn azon felajánlások sorszámát, amelyek a bejárat bal és jobb
oldalán található ágyást is beültetnék! A sorszámokat egy-egy szóközzel válassza el
egymástól! 
'''
print('3.feladat')
osszegzo_cikl = 0
sorszamok = []

while osszegzo_cikl < len(elso):
    
    if elso[osszegzo_cikl] - utolso[osszegzo_cikl] > 0:
        sorszamok.append(osszegzo_cikl + 1)
    
    osszegzo_cikl += 1

print(f'A bejarat mindket oldalara ultetok: {", ".join(map(str,sorszamok))}\n')

'''
4.feladat
Kérje be a felhasználótól egy ágyás sorszámát! A tesztelés során használhatja az 1. ágyást, 
amelyet többen is beültetnének és a 269. ágyást, amelynek beültetésére senki sem vállalkozik.
a) Írja a képernyőre, hogy hány felajánlásban szerepel ez az ágyás!
b) Adja meg, milyen színű lesz ez az ágyás, ha mindenki a felajánlások
sorrendjében végzi el az ültetést, de nem ültet, ha másvalaki előtte már ültetett
oda! Ha nem ültetett oda senki, akkor „Ezt az ágyást nem ültetik be.” szöveget
jelenítse meg!
c) Adja meg, milyen színekben pompázna ez az ágyás, ha az eredeti tervvel
ellentétesen minden felajánló elültetné virágait! Minden színt csak egyszer
tüntessen fel! Az egyes színeket szóközökkel válassza el egymástól! Ha nem
ültettek oda virágot, ne jelenítsen meg semmit! 
'''
print('4.feladat')
'''bekero_cikl = 0
while bekero_cikl == 0:
    agyas_szam = input('Adja meg az agyas sorszamat! ')
    if agyas_szam.isdigit():
        agyas_szam = int(agyas_szam)
        if agyas_szam <= viragagyasok:
            bekero_cikl += 1
'''
agyas_szam = 100
szin = []

felajanlok = 0
fel_cikl = 0
while fel_cikl < len(elso):
    if agyas_szam in range(elso[fel_cikl], utolso[fel_cikl]):
        felajanlok += 1

        if szinek[fel_cikl] not in szin:
            szin.append(szinek[fel_cikl])

    fel_cikl += 1

print(f'A felajanlok szama: {felajanlok}')

elso_cikl = 0
while elso_cikl < len(elso):
    if agyas_szam in range(elso[elso_cikl], utolso[elso_cikl]):
        print(f'A viragagyas szine, ha csak az elso ultet: {szinek[elso_cikl]}')
        break
    elif felajanlok == 0:
        print('Ezt az agyast nem ultetik be')
        
    elso_cikl += 1


print(f'A viragagyas szinei: {" ".join(map(str,szin))}\n')


'''
5.feladat
A felajánlások alapján több eset lehetséges. Határozza meg, melyik teljesül! Az idézőjelek
közötti szöveget írja a képernyőre!
• „Minden ágyás beültetésére van jelentkező.”
• Ha nincs minden ágyásra jelentkező, de a felajánlásokban vállalt ágyások
számának összege nagyobb vagy egyenlő, mint, az ágyások száma, akkor:
„Átszervezéssel megoldható a beültetés.”
• Ha kevesebb ágyás beültetésére vállalkoztak, mint amennyi van: „A beültetés
nem oldható meg.”
'''
print("5.feladat")

bejaro_cikl = 0
nincs_ultetve = 0
for i in range (0, viragagyasok + 1):
    while bejaro_cikl < len(elso):
        if i not in range(elso[bejaro_cikl], utolso[bejaro_cikl]):
            nincs_ultetve += 1



        bejaro_cikl += 1

felajanlasok_cikl = 0
ultetett = []

while felajanlasok_cikl < len(elso):
    if elso[felajanlasok_cikl] - utolso[felajanlasok_cikl] < 0:
        ultetett.append(abs(utolso[felajanlasok_cikl] - elso[felajanlasok_cikl]))
    
    elif elso[felajanlasok_cikl] - utolso[felajanlasok_cikl] > 0:
        ultetett.append(viragagyasok - elso[felajanlasok_cikl] + utolso[felajanlasok_cikl])
    
    felajanlasok_cikl += 1


if nincs_ultetve == 0:
    print('Minden agyas beultetesere van jelentkezo')
elif  sum(ultetett) >= viragagyasok:
    print('Atszervezessel megoldhato a beultetes.')
else:
    print('A beultetes nem oldahato meg')

