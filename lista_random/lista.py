# lista létrehozása, hosszát bekérni, feltölteni random számokkal, kiirjuk a legnagyobb számokat, bekérünk egy számot szerepel e a listában


import os
import platform
import random
import time


def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    return torles


torles()
lista = []

# bekerjük a lista hosszat


def start():
    print('----------------------------')
    print('       Lista program')
    print('----------------------------')


start()

bekero_ciklus = 0

while bekero_ciklus == 0:
    lista_hossz = input('Milyen hosszu listat szeretnel csinalni? ')

    if lista_hossz.isdigit():
        lista_hossz = int(lista_hossz)
        bekero_ciklus += 1
        time.sleep(2)

        torles()

    else:
        print('Rossz bemeneti erteket adtal meg!')
        print('Kerlek probald ujra')


lista_elemek = 0

while lista_elemek < lista_hossz:
    lista.append(random.randint(-100, 100))
    lista_elemek += 1

print('A feltoltés kesz!\n')
time.sleep(2)


#max

def legnagyobb(lista):
    torles()
    print(f'A legnagyobb szam a {max(lista)}')

    return legnagyobb






#kereses





def szerepel(lista):
    torles() 
    szambe_ciklus = 0

    while szambe_ciklus == 0:
        szam = input('Melyik szamot szeretned keresni? ')

        if szam.isdigit():
            szam = int(szam)
            szambe_ciklus += 1
        
    
    
    if szam in lista:
        print(
            f'Az altalad keresett szam a {lista.index(szam) + 1}. helyen szerepel a listaban')
    else:
        print('A keresett szam nincs a listaban')

    return szerepel





#min

def legkisebb(lista):
    torles()
    print(f'A legkisebb szam a {min(lista)}')
   
    return legkisebb


#hozzafűz

def hozzarak(lista):
    torles()
    hozza_cikl = 0

    while hozza_cikl == 0:

        hozza = input('Milyen szamot szeretnel a listahoz fuzni? ')
        if hozza.isdigit():
            hozza = int(hozza)
            lista.append(hozza)
            hozza_cikl += 1

            time.sleep(2)
            print('kesz!')
        
        else:
            print('A bemenet nem szam!')
        
        return hozzarak

#kiirat

def kiiras(lista):
    print(lista)
    return kiiras






#az UI kezdete
 


ui_cikl = 0


print('A program az alabbi lehetosegek kozul tud dolgozni!\n')
print('1 - minimum szam keresese')
print('2 - maximum szam keresese')
print('3 - egy adott szam keresese a listaban')
print('4 - lista kiiratasa')
print('5 - lista feltoltese egy alltalad kivalasztott szammal\n')

time.sleep(2)

while ui_cikl == 0:
    mit_akar = input('Mit szeretne lefuttatni?')

    if mit_akar.isdigit():
        mit_akar = int(mit_akar)
        if mit_akar <= 5:
            ui_cikl += 1


        if mit_akar == 1:
            legkisebb(lista)
        elif mit_akar == 2:
            legnagyobb(lista)
        elif mit_akar == 3:
            szerepel(lista)
        elif mit_akar == 4:
            kiiras(lista)
        elif mit_akar == 5:
            hozzarak(lista)
    
    
    else:
        print('Kerlek szamot irj be!')


