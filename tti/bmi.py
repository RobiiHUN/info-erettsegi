'''
Kérdezze meg a program, hogy a betöltött adatok közül melyiket szeretné lelistáztatni. (név, testm, testsúly)
'''

import os, platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')




if os.path.exists('testadatok.txt'):
    testadatok = open('testadatok.txt', 'r')
else:
    print('nem talalom a fajlt')




ember = {}
nevek  = []
magassagok = []
tomegek = []


for sor in testadatok:

    ember_adatai = sor.split()
    ember['nev'] = ember_adatai[0]
    ember['magassag'] = ember_adatai[1]
    ember['suly'] = ember_adatai[2]

    nevek.append(ember['nev'])
    magassagok.append(ember['magassag'])
    tomegek.append(ember['suly'])


#az infinity loop-ok szamlaloi

loop1 = 1
loop2 = 1
loop3 = 1
loop4 = 1
loop5 = 1

#menu rendszer letrehozasa

while loop4 == 1:


    while loop1 == 1:
        adat_v_lista = input('Egy kokret adatot szeretne kiiratni v listat? (a;l)')

        if adat_v_lista == 'a' or adat_v_lista == 'l':
            loop1 += 1

    # a lista ag vizsgalata
    if adat_v_lista == 'l':
        while loop2 == 1:

            kerdes = input('A betoltott adatok kozul melyiket szeretne kiiratni?(nev, magassag, tomeg) ')

            if kerdes == 'nev':
                print(f'A kert elemek: {nevek} ')
                loop2 += 1
            
            elif kerdes == 'magassag':
                print(f'A kert lista: {magassagok}')
                loop2 += 1
        
            elif kerdes == 'tomeg':
                print(f'A kert lista: {tomegek}')
                loop2 += 1

    else: 
        while loop3 == 1:
            kert_nev = input('Kérlek írj be egy nevet, aki szerepel a listaban!')

            for tagok in nevek:
                if tagok == kert_nev:
                    loop3 += 1
                    kert_nev_index = nevek.index(kert_nev)
        print(f'Az altalad kert szemelyt {kert_nev}nek hivjak, {tomegek[kert_nev_index]}kg nehez, es {magassagok[kert_nev_index]}cm magas.')

    vegso = input('Ki szeretnel lépni? (i,n)')

    if vegso == 'i':
        loop4 += 1
    elif vegso == 'n':

            #kijelzo torles

        if platform.system() == 'Windows':
             os.system('cls')
        else:
            os.system('clear')

        while loop5 == 1:
            fajlba = input('Ki szeretned iratni az adatokat egy fileba?(i,n)')
        
            if fajlba == 'i':
                print('Rendben rajta vagyok....')

                if os.path.exists('kiiratas.txt'):
                    kiir = open('kiiratas.txt', 'w')
                else:
                    print('nem talalom a fajlt')


                print('Az adatok az alabbiak: ', file = kiir)

                n = 0
                #indexé alakítas
                while n < len(nevek)-1:
                    print(nevek[n], magassagok[n], tomegek[n], file = kiir)
                    n  += 1
                loop5 += 1
            else:
                loop5 += 1

testadatok.close()



   