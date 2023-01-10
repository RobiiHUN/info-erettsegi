import os
import platform
import random


def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
torles()


fo_cikl = 0

while fo_cikl == 0:

    #bekeres

    bekero_cikl = 0
    while bekero_cikl == 0:
        lefut_beker = input('Hanyszor szeretne lefuttatni? (1-10)')

        if lefut_beker.isdigit():
            lefut_beker = int(lefut_beker)
            if lefut_beker > 0 and lefut_beker <= 10:
                bekero_cikl += 1
    
    torles()
    print(f'Menetek szama: {lefut_beker}')

    #dobalasok
    
    peti =[]
    robi = []

    dobas = 0
    while dobas < lefut_beker:
        peti.append(random.randint(1,7))
        robi.append(random.randint(1,7))
        dobas += 1
    
    #print(peti)
    #print(robi)

    #pontszamítás
    nyer = 0

    pont_cikl = 0
    while pont_cikl < lefut_beker:
        if robi[pont_cikl] > peti[pont_cikl]:
            nyer += 1
        elif robi[pont_cikl] < peti[pont_cikl]:
            nyer -= 1

        pont_cikl += 1
        
    #print(nyer)

    if nyer < 0:
        print(f'A vegso nyertes Peti, {abs(nyer)} ponttal')
    elif nyer > 0:
        print(f'A vegso nyertes Robi, {nyer} ponttal')
    else:
        print(f'A jatek dontetlen volt')







    fo_cikl += 1


