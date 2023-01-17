import os, platform, datetime

def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

torles()

#szemelyi bekeres

bekero_cikl = 0

szemelyi_sz = str(1991011700)
#print(szemelyi_sz)

'''
while bekero_cikl == 0:
    szemelyi_sz = input('Irja be a szemelyazonositoja elso 10 jegyet: ')
    if szemelyi_sz.isdigit() and len(szemelyi_sz) == 10:
        szemelyi_sz = str(szemelyi_sz)
        bekero_cikl += 1

        '''
    
#ferfi v no

szul_ev = int(szemelyi_sz[1:3])
#print(szul_ev)

if szul_ev >= 97 and szul_ev <= 99 and int(szemelyi_sz[0]) == 1:
    neme = 'ferfi'
elif szul_ev >= 97 and szul_ev <= 99 and int(szemelyi_sz[0]) == 2:
    neme = 'no'
elif szul_ev < 97 and int(szemelyi_sz[0]) == 3:
    neme = 'ferfi'
elif szul_ev < 97 and int(szemelyi_sz[0]) == 4:
    neme = 'no'

print(f'Az adott szemely : {neme}')


#szemely szuletesi sorszama

sorszam = int(szemelyi_sz[7:10])
print(f'A szemely sorszama : {sorszam}')

#hany eves

jelenlegi_ev = datetime.date.today().year

if szul_ev >= 97:
    szul_ev += 1900
else:
    szul_ev += 2000

hany_eves = jelenlegi_ev - szul_ev
print(f'A megadott szemely {hany_eves} eves.')


szemelyi_sz2 = str(3041011700)
'''
while bekero_cikl == 0:
    szemelyi_sz2 = input('Irja be a szemelyazonositoja elso 10 jegyet: ')
    if szemelyi_sz2.isdigit() and len(szemelyi_sz2) == 10:
        szemelyi_sz2 = str(szemelyi_sz2)
        bekero_cikl += 1

        '''

szul_ev2 = int(szemelyi_sz2[1:3])

if szul_ev2 >= 97:
    szul_ev2 += 1900
else:
    szul_ev2 += 2000

hany_eves2 = jelenlegi_ev - szul_ev2

#idosebb e

if hany_eves > hany_eves2:
    print('Az elso szemely az idosebb')
elif hany_eves2 > hany_eves:
    print('A masodik szemely az idosebb')
elif hany_eves == hany_eves2 and int(szemelyi_sz[7:10]) < int(szemelyi_sz2[7:10]):
    print('Az elso szemely az idosebb')
elif hany_eves == hany_eves2 and int(szemelyi_sz[7:10]) > int(szemelyi_sz2[7:10]):
    print('A masodik szemely az idosebb')

#korkulonbseg

kulobseg = hany_eves - hany_eves2

if kulobseg < 0:
    print(f'A korkulonbseg {abs(kulobseg)} ev.')
if kulobseg > 0:
    print(f'A korkulonbseg {kulobseg} ev.')

#11.szam kiszamitasa


szamok_szorzastalan = []

for i in range(10):
    szamok_szorzastalan.append(int(szemelyi_sz2[i]))


szamok = []
szamok_tiztol = []

visszaszamlalo = 10
while visszaszamlalo > 0:
    szamok_tiztol.append(visszaszamlalo)
    visszaszamlalo -= 1


   
for szam in szamok_szorzastalan:
    szamok.append(szam * szamok_tiztol[szamok_szorzastalan.index(szam)])


tizenegyedik = sum(szamok) % 11

if tizenegyedik == 10:
    print('Hibas a szuletesi datum')
else:
    int_szemely = int(szemelyi_sz2)
    int_szemely += tizenegyedik

print(f'A teljes szemelyazonosito szamod: {int_szemely}')