import os
import platform
import random
def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    

torles()
szamok = []
bekertek = []


vegt_cikl = 0

while vegt_cikl == 0:

    #5
    def otos(szamok):
        szamok.clear()

        huzas_cikl5 = 0

        while huzas_cikl5 < 5:
            szam = random.randint(1,90)
            if szam not in szamok:
                szamok.append(szam)
                huzas_cikl5 += 1

        szamok.sort()
        #print(f'Az otos lotto eheti nyeroszamai: {szamok}\n')
        return szamok

    #6
    def hatos(szamok):
        szamok.clear()
        huzas_cikl6 = 0


        while huzas_cikl6 < 6:
            szam = random.randint(1,45)
           
            if szam not in szamok: 
                szamok.append(szam)
                huzas_cikl6 += 1
        
        szamok.sort()
        #print(f'A hatos lotto eheti nyeroszamai: {szamok}\n')
        return szamok

    #szamok bekerese
    def bekert_szamok(bekertek, menu):
        bekertek.clear()
        
        if menu == 5:
            print('Kerek 5 szamot, 1 es 99 kozott!')
        else:
            print('Kerek 6 szamot 1 es 45 kozott!')

        szam_szamlalo = 0
        while szam_szamlalo < menu:
            if menu == 5:
                bekert = input(f'Kerem a/az {szam_szamlalo + 1}. szamot! ')
                if bekert.isdigit():
                    bekert = int(bekert)
                    if bekert >= 1 and bekert <= 99:
                        bekertek.append(bekert)
                        szam_szamlalo += 1
            else:
                bekert = input(f'Kerem a/az {szam_szamlalo + 1}. szamot! ')
                if bekert.isdigit():
                    bekert = int(bekert)
                    if bekert >= 1 and bekert <= 45:
                        bekertek.append(bekert)
                        szam_szamlalo += 1

        bekertek.sort()
        return bekertek, menu
    

    

    def nyert(bekertek, szamok):
        db_nyert = 0 
        
        for bekert in bekertek:
            if bekert in szamok:
                db_nyert += 1
        
        print(f'\nA tippjeid kozul {db_nyert} talalat volt\n')


    #kivalasztja h 5 v 6

    bekero_cikl = 0

    while bekero_cikl == 0:
        menu = input('Otos vagy hatos lottot szeretne jatszani?(5/6) ')
        if menu.isdigit():
            menu = int(menu)
            if menu == 5 or menu == 6:
                bekero_cikl += 1
        else:
            print('kerlek csak 5-s vagy 6-s szamot uss!')

    if menu == 5:
        otos(szamok)
        torles() 
        print(szamok)
        bekert_szamok(bekertek, menu)
        nyert(bekertek, szamok)

    else:
        hatos(szamok)
        torles()
        print(szamok)
        bekert_szamok(bekertek, menu)
        nyert(bekertek, szamok)



#lefutas, infinity loop vege

    lefutas_cikl = 0

    while lefutas_cikl == 0:
        lefut = input('Szeretne megegyszer lefuttatni a programot? (i/n)')
        if lefut == "i" or lefut == 'n':
            lefutas_cikl += 1 
       
    if lefut == 'i':
        torles()
        print('Rendben!\n')
    else:
        vegt_cikl += 1
