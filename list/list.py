'''
#1-es faladat

for i in range(1,40):
    if i % 3 == 0:
        print(i)

#2-es feladat
print("----------------------------------")


szavak = ['ajto','tojas','Otto','Tamas', 'tep','Tesla','alma','python']
t_betus_szavak = []
for t_betu in szavak:
    if t_betu.startswith('t') or t_betu.startswith('T'):
        if True:
            print(t_betu)
            t_betus_szavak.append(t_betu)
            

#3-as feladat
print("----------------------------------")

print(t_betus_szavak)


#4-es feladat
print("----------------------------------")

szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]

for x in szamok:
    if x % 3 == 0 and x % 2 == 0:
        if True:
            print(x)







mondat = input("Kerek egy mondatot: ")


if mondat[-1] == ".":
    print("Ez a mondat egy kijelento mondat!")
elif mondat[-1] == "?":
    print("Ez a mondat egy kerdo mondat!")
elif mondat[-1] == "!":
    print("Ez a mondat egy felkialto mondat")
else:
    print("Nem tudtam beazonositani a mondat tipusat")





szinek = ["sarga","zold", "piros", "sarga"]

bekert = input("Kerek egy szint: ")



if bekert in szinek:
    print("A szin mar tagja a listanak!")
    szinek.append(bekert)
    print(szinek)
    counter = szinek.count(bekert)
    print()
    print(f'Az altalad beirt szam {counter}-szer szerepel a listaban')
    
'''
import random 
szamok = []

n = 0
while n < 10:
    n = n+1
    szam=random.randrange(1,3)
    szamok.append(szam)

szamok.sort()

egyes = szamok.count(1)
kettes = szamok.count(2)
ossz = egyes + kettes

while egyes > 1:
    egyes = egyes-1
    szamok.remove(1)
  
while kettes > 1:
    kettes = kettes-1
    szamok.remove(2)

print(szamok)