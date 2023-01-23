import os,platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


"""
1. A mintának megfelelően kérjen be a felhasználótól egy legalább 5 jegyű egész
számot! Az adatbekérés mindaddig folytatódjon, amíg a megadott szám
számjegyeinek száma legalább 5 nem lesz!
"""

bekero_cikl = 0
while bekero_cikl == 0:
    szam = input('Adj meg legalabb 5 szamjegybol allo szamot! ')
    
    if len(szam) >= 5 and szam.isdigit():
        szam = int(szam)
        break


"""
2. Vizsgálja meg és a mintának megfelelően jelezze, hogy a megadott szám osztható-e
öttel és tízzel egyidejűleg!
"""
print('\n2.feladat')

if szam % 5 == 0 and szam % 10 == 0:
    print('A szam osztahto ottel es tizzel.')
else:
    print('A szam nem oszthato se ottel, se tizzel.')


"""
3. A minta szerint visszafelé olvasva jelenítse meg a megadott számot!
"""    
print('\n3.feladat')

szam = str(szam)
visszafele = []
vissza_cikl = len(szam)

while vissza_cikl > 0:
    visszafele.append(szam[vissza_cikl - 1])
    
    vissza_cikl -= 1

print(f'A szam visszafele olvasva: {"".join(map(str,visszafele))}')

"""
4. Egy listába gyűjtse ki, és a mintának megfelelően emelkedő sorrendben jelenítse a
páros számjegyeket!
"""
print('\n4.feladat')
paros = []
for szamjegy in szam:
    if int(szamjegy) % 2 == 0:
        paros.append(szamjegy)

paros.sort()

print(f'A paros szamjegyek novekvo sorrendben: {", ".join(map(str, paros))}')


"""
5. A minta szerint jelenítse meg az ismétlődő számjegyeket! Minden számjegy csak
egyszer kerüljön kiírásra!
"""
print('\n5.feladat')
ismetlodo = []


for szamjegy in str(szam):
    if szam.count(szamjegy) > 1 and szamjegy not in ismetlodo:
        ismetlodo.append(szamjegy)



if len(ismetlodo) == 0:
    print('Nincs ismetlodo szam')
else:
    print(f'Az ismetlodo szamjegyek: {", ".join(map(str, ismetlodo))}')

"""
6. Maszkolt formában jelenítse meg a megadott számot! Az egyes számjegyek helyén
'x' betű szerepeljen, az ezres csoportokat pedig pont válassza el a mintának
megfelelően!
"""    
print('\n6.feladat')