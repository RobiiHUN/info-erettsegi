import os
import platform
import random
 
def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    

torles()

#5 kockabol kivalasztunk 2-t

dobott_szamok = []

            # ismetlodes kicsillapizalasa
while len(dobott_szamok) < 5:
    generalt_szam = random.randint(1,6)
    dobott_szamok.append(generalt_szam)

#print(dobott_szamok)

#2 kivalasztasa, ismetlodes nelkul


kivalasztott = []

while len(kivalasztott) < 2:
    generalt_szam = random.randint(0,4)
    if dobott_szamok[generalt_szam] not in kivalasztott:
        kivalasztott.append(dobott_szamok[generalt_szam])

#print(kivalasztott)

osszeg = 0
for elem in kivalasztott:
    osszeg += elem

print(f'Az elso dobas: {osszeg}')

#2.dobas
dobott_szamok_2 = []

            # ismetlodes kicsillapizalasa
while len(dobott_szamok_2) < 5:
    generalt_szam = random.randint(1,6)
    dobott_szamok_2.append(generalt_szam)

#2 kivalasztasa, ismetlodes nelkul


kivalasztott_2 = []

while len(kivalasztott_2) < 2:
    generalt_szam = random.randint(0,4)
    if dobott_szamok_2[generalt_szam] not in kivalasztott_2:
        kivalasztott_2.append(dobott_szamok_2[generalt_szam])

osszeg_2 = 0
for elem in kivalasztott_2:
    osszeg_2 += elem

print(f'A masodik dobas: {osszeg_2}')


# "come out roll"

def come_out_roll(osszeg, osszeg_2):
    bekero_cikl = 0
    
    while bekero_cikl == 0:
        bekert = input('Szerinted a dobas eredmenye 7 vagy 11 lesz? (y,n) ')
        if bekert == 'y' or bekert == 'n':
            bekero_cikl += 1

    
    if osszeg == 2 or osszeg == 3 or osszeg == 12:
        print('Vesztettel')
    elif osszeg == osszeg_2 and bekert == 'y':
        print('A penzed duplajat nyerted')
    elif osszeg_2 == 7 and bekert == 'y':
        print('Vesztettel')


    if bekert == 'n' and osszeg == 2:
        print('Nem nyertel, de a penzed megtarthatod')
    elif bekert == 'n' and osszeg == 3:
        print('A penzed duplajat nyerted')
    elif bekert == 'n' and osszeg == 7 or osszeg == 11:
        print('Vesztettel')
    elif bekert == 'n' and osszeg == 12 or osszeg_2 == 12:
        print('Nem nyertel, de a penzed megtarthatod')


come_out_roll(osszeg, osszeg_2)

