import os, platform,random

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


print("1.feladat")

#bekerjuk a szamot

bekero_cikl = 0
while bekero_cikl == 0:
    dob_szam = input("Add meg a dobások szamat! ")

    if dob_szam.isdigit():
        dob_szam = int(dob_szam)
        bekero_cikl += 1



print("\n2.feladat")


dobasok = []

#for ciklus most az egyszer

for lepes in range(dob_szam):
    dobasok.append(random.randint(1,6))

print(f'A dobasok: {dobasok}')



print("\n3. feladat")

#atlag szamitas
#osszeadjuk oket majd elosztjuk a db-szammal

atlag = sum(dobasok)/len(dobasok)
print(f'A jatekos atlagosan {atlag} mezot, osszesen {sum(dobasok)} mezot haladt elore.')





print("\n4.feladat")

#6-osok szama

hatosok = dobasok.count(6)
if hatosok > 0:
    print(f'A jatekos {hatosok} dobott hatost')
else:
    print("A jatekos nem dobott hatost")



print("\n5.feladat")


paros_szamok = dobasok.count(2) + dobasok.count(4) + dobasok.count(6)
print(f'A jatekos {paros_szamok} alkalommal dobott paros szamot.')


print("\n6.feladat")

# megizsgaljuk a szamokat az 1-es indexutol
vizsg_cikl = 1
alkalmak = 0

while vizsg_cikl < len(dobasok):
    if dobasok[vizsg_cikl - 1] < dobasok[vizsg_cikl]:
        alkalmak += 1
    vizsg_cikl+= 1

print(f'A jatekos {alkalmak} alkalommal dobott kevesebbet, mint az elozo korben')