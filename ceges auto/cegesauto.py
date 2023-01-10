import os
import platform
 
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')
 
 
if os.path.exists('autok.txt'):
    fajl = open('autok.txt', 'r')
else:
    print('nem talalom a fajlt')
 
 
#2.feladat
print('2.feladat')
 
auto = {}
datumok = []
idok = []
rendszamok = []
azonositok = []
km_orak = []
ki_be = []
 
#adatok betöltése
 
for sor in fajl:
    auto_adatok = sor.split()
    auto['datum'] = auto_adatok[0]
    auto['ido'] = auto_adatok[1]
    auto['rendszam'] = auto_adatok[2]
    auto['ID'] = auto_adatok[3]
    auto['km'] = auto_adatok[4]
    auto['ki/be_hajtas'] = auto_adatok[5]
 
    datumok.append(int(auto['datum']))
    idok.append(auto['ido'])
    rendszamok.append(auto['rendszam'])
    azonositok.append(int(auto['ID']))
    km_orak.append(int(auto['km']))
    ki_be.append(int(auto['ki/be_hajtas']))
 
#a ki hajtásoknak csinálunk egy listát
 
szamlalo = 0
ki_index = []
 
for ki in ki_be:
   
 
    if ki == 0:
        ki_index.append(szamlalo)
    szamlalo += 1
 
#2.feladat kiiratás
 
print(f'{datumok[max(ki_index)]}.nap rendszám: {rendszamok[max(ki_index)]}')
 
#3 feladat
print('3.feladat')
 
loop1 = 0
 
#bekerjuk a napot
 
#ki kell venni!!!!
nap_be = 4
 
 
 
'''
while loop1 == 0:
    nap_be = input('Nap: ')
 
    if nap_be.isdigit():
        nap_be = int(nap_be)
        if nap_be <= max(datumok) and nap_be > 0:
            loop1 += 1
 
'''
 
 
 
print(f'Forgalomban a {nap_be}. napon:')
nap_be_index = datumok.index(nap_be)
 
 
nap_forgalom = []
 
 
#index kereses
 
for ido in datumok:
    if ido == nap_be:
        nap_forgalom.append(nap_be_index)
        nap_be_index += 1
 
 
#ki/be lista létrehozása
 
ki_be_str = []
 
for elem in ki_be:
    if elem == 0:
        ki_be_str.append('ki')
    else:
        ki_be_str.append('be')
 
# 3.feladat kiiratas
 
for nap in nap_forgalom:
    print(f'{idok[nap]} {rendszamok[nap]} {azonositok[nap]} {ki_be_str[nap]} ')
 
 
 
#4.es feladat
print('4.feladat')
 
ki = 0
be = 0
 
for be_vagy_ki in ki_be:
    if be_vagy_ki == 0:
        ki += 1
    else:
        be += 1
 
print(f'A hónap végén {ki-be} kocsit nem hoztak vissza')
 
#5.feladat
print('5.feladat')
 
#összegyűjtjük a rendszámokat
kocsik = []
 
for rendszam in rendszamok:
    if rendszam not in kocsik:
        kocsik.append(rendszam)
   
kocsik.sort()  
 
szamlalo2 = 0
elso_kocsi = 0
 
 
for rendszam in rendszamok:
   
   
    if ki_be[szamlalo2] == 1 and rendszam == kocsik[0]:
        elso_kocsi += km_orak[szamlalo2]
 
    elif ki_be[szamlalo2] == 0 and rendszam == kocsik[0]:
        elso_kocsi -= km_orak[szamlalo2]
   
    szamlalo2 += 1
 
print(f'{kocsik[0]} {elso_kocsi} km')
 
 
#6.feladat
print('6.feladat')
 
#emberek csoportosítása
 
emberek = []
 
for szemely in azonositok:
    if szemely not in emberek:
        emberek.append(szemely)
 
emberek.sort()
 
utak = []
 
szamlalo4 = 0
 
#embereenkénti szortírozás beágyazó ciklussal
 
 
while szamlalo4 < len(emberek):
 
    szamlalo3 = 0
 
    while szamlalo3 < len(azonositok):
        if azonositok[szamlalo3] == emberek[szamlalo4]:
            utak.append(km_orak[szamlalo3])
 
 
        szamlalo3 += 1
 
    szamlalo4 += 1
 
 
#különgyűjtjük a ki és visszahozatali km-ereket
 
szamlalo5 = 0
ki_vitelkor = []
vissza = []
 
while szamlalo5 < len(utak):
    if szamlalo5 % 2:
        vissza.append(utak[szamlalo5])
    else:
        ki_vitelkor.append(utak[szamlalo5])
 
    szamlalo5 += 1
 

 
 
# a ki és visszahozatali km-erek különbsége tárolása egy listában
 
beletett_km = []
 
for vissza_km in vissza:
    if vissza_km-ki_vitelkor[vissza.index(vissza_km)] > 0:
        beletett_km.append(vissza_km-ki_vitelkor[vissza.index(vissza_km)])
 


 
 
#    MIÉRT NEM FUT LE????????????????  


#7.feladat
print('7.feladat')

menetlevel = open('X_menetlevel.txt', 'w') 
szamlalo6 = 0

while szamlalo6 < 1:
    rendszam_bekert = input('Rendszám: ')

    if rendszam_bekert in rendszamok:
        
        
        
        
        index_bekert = []
        index_szamlalo = 0

        for rendszam in rendszamok:
            if rendszam == rendszam_bekert:
                
                index_bekert.append(index_szamlalo)
                

            index_szamlalo += 1



        # print(index_bekert)

        for index in index_bekert:
            if index_bekert.index(index) % 2:
                

                
                menetlevel.write(f'{azonositok[index]} {datumok[index]} {idok[index]} {km_orak[index]} {datumok[index + 1]} {idok[index + 1]} {km_orak[index + 1]} ')
        
        
        
        
        print('Menetlevél kész')
        szamlalo6 += 1





    