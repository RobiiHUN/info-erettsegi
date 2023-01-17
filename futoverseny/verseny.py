import os, platform

def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

torles()

"""
1. Tárolja el az alábbi versenyszakaszokat a megadott sorrendben:
'F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF0', 'F2.1', 'NF2'
"""

szakaszok = ['F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF0', 'F2.1', 'NF2']

"""
2. A mintának megfelelően adja meg, hogy hány km volt a versenytáv?
"""

print('2.feladat')

verseny_hossz = 0
for szakasz in szakaszok:
    if szakasz[0] == 'F':
        verseny_hossz += float(szakasz[1:])
    else:
        verseny_hossz += float(szakasz[2:])

print(f'A verseny tavja {verseny_hossz} km volt.\n')


"""
3. A mintának megfelelően adja meg, hogyan ért be a célba Olivér, futva vagy
gyalogolva?
"""
print('3.feladat')

utolso_db = szakaszok[len(szakaszok) - 1]
#print(utolso_db)


if utolso_db[0] == 'N' and utolso_db[1] == 'F':
    if int(utolso_db[2:]) > 0:
        print('Gyalog ert celba.\n')

else:
    print('Futva ert celba.\n')



"""
4. Vizsgálja meg, és a mintának megfelelően jelezze, hogy hány alkalommal állt meg a
Olivér a verseny közben.
"""
print('4.feladat')

megallas_szam = 0
for szakasz in szakaszok:
    if szakasz[0:2] == 'NF' and szakasz[2:] == '0':
        megallas_szam += 1

print(f'A verseny soran {megallas_szam} alkalommal allt meg.\n')

"""
5. A mintának megfelelően adja meg, hogy a verseny alatt hány alkalommal szakította
meg a futását! (Ha futott majd gyalogolt és megállt, majd ismét futni kezdett, ez csak
egy megszakításnak számít!)
"""

print('5.feladat')

megszakitas = 0
bejaro_cikl = 0

while bejaro_cikl < len(szakaszok) - 1:
    if szakaszok[bejaro_cikl][0] == 'F' and not szakaszok[bejaro_cikl + 1][0] =='F':
        megszakitas += 1
    bejaro_cikl += 1

print(f'A futasat {megszakitas} alkalommal szakította meg.\n')

"""
6. Vizsgálja meg, és a mintának megfelelően jelezze, hogy volt-e olyan alkalom, hogy
gyaloglás után közvetlenül megállt.
"""

print('6.feladat')

gyaloglas = 0
vizsg_cikl = 0

while vizsg_cikl < len(szakaszok) - 1:
    if szakaszok[vizsg_cikl][0:2] == 'NF' and szakaszok[vizsg_cikl + 1] =='NF0':
        gyaloglas += 1
    vizsg_cikl += 1

if gyaloglas > 0:
    print('Volt olyan alkalom, hogy gyaloglas utan megallt.')
else:
    print('Nem vol olyan alkalom, hogy gyaloglas utan megallt volna.')



#      40 perc volt