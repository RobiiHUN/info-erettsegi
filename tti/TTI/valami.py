
import time



nevek = ['pityu','petti', 'anyu']
tomegek_str = ['63', '175', '80']
magassagok_cm = ['160','210', '175']


magassagok = [int(x) / 100 for x in magassagok_cm] 
tomegek=[ int(x) for x in tomegek_str]


if len(nevek) == len(magassagok) == len(tomegek):
    n = 0
    for nev in nevek:
        tti = tomegek[n] / (magassagok[n] * magassagok[n])
        if tti < 18:
            tti_ert = "koros sovanysag"
        elif tti < 25:
            tti_ert = "normalis"
        elif tti < 30:
            tti_ert = "tulsuly"
        else:
            tti_ert="elhizas"
       
else:
    print("a listadbol hianyzik vmi")            

#0-ik feladat:


print("------------------------------------")
print("TTI rendszer")
print("------------------------------------")





time.sleep(3)
be_vagy_ki = input("Lekerdezni szeretnel vagy feltolteni?(Eleg ha csak kezdobetut irsz)")



   

#Feladat: Kérjünk be egy sorszámot, amelynek megfelelő adatokat jelenítünk meg.



if be_vagy_ki == "l":
    index = int(input('Melyik rekordot irjuk ki? '))

    if index > 0 and index <= len(nevek):
        tti = tomegek[index-1] / (magassagok[index-1] * magassagok[index-1])
        print(f'{index}. {nevek[index-1]} {magassagok[index-1]}cm {tomegek[index-1]}kg tti: {tti:.2f}')


    else:
        print('Nincs ilyen rekord!')

elif be_vagy_ki == "f":
    print("")
    print("Rendben! Pillanat, mert kicsit lassu vagyok :)")
    time.sleep(2)
    print("")


    hozza_nev = input("Kerem a nevet: ")
    hozza_tomeg = int(input("Kerem az egyen sulyat!(kg)"))
    hozza_magassag = int(input("Kerem az egyen magassagat!(cm)"))
    print("")
    print("")


    nevek.append(hozza_nev)
    tomegek_str.append(hozza_tomeg)
    magassagok_cm.append(hozza_magassag)

    print(f'{hozza_nev} {tti_ert} TTI ertekkel rendelkezik.')
    print("")

    vegso_kiiras = input("Szeretnel kiiratni egy rekordot? (i vagy n)")

    if vegso_kiiras == "i":
        index = int(input('Melyik rekordot irjuk ki? '))

        if index > 0 and index <= len(nevek):
            tti = tomegek[index-1] / (magassagok[index-1] * magassagok[index-1])
            print(f'{index}. {nevek[index-1]} {magassagok[index-1]}cm {tomegek[index-1]}kg tti: {tti:.2f}')


        else:
            print('Nincs ilyen rekord!')
    elif vegso_kiiras == "n":
        print("Rendben!")
        time.sleep(2)
        print("Koszi, hogy a programomat hasznaltad!")




    
    

else:
    print("Szerintem elgepeltel vmit, ilyen parancs nincs!")

