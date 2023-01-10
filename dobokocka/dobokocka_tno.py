import random
print('dobókocka')
#roby és peti...1 dobás... aki többet dob, nyer...
# felhasználótról bekérni a menetek számát
# megszámoljuk, hogy ki hányszor nyer
# menetenként kell vizsgálni
# végén írja ki, hogy ki hányszor nyert és ki a győztes
menetek_szama=int(input('Add meg a menetek számát!'))
print(f';Menetek száma: {menetek_szama}')
robi_nyert=0
peti_nyert=0
for i in range(menetek_szama):
    robi_kocka_1=random.randint(1,7)
    robi_kocka_2=random.randint(1,7)
    robi_kocka_3=random.randint(1,7)
    robi_osszesen=robi_kocka_1+robi_kocka_2+robi_kocka_3
    peti_kocka_1=random.randint(1,7)
    peti_kocka_2=random.randint(1,7)
    peti_kocka_3=random.randint(1,7)
    peti_osszesen=peti_kocka_1+peti_kocka_2+peti_kocka_3
    if robi_osszesen'gt;peti_osszesen:
        print(f'#39;Robi dobásainak értéke: {robi_kocka_1}, {robi_kocka_2},
{robi_kocka_3}'#39;)
        print(f'#39;Peti dobásainak értéke: {peti_kocka_1}, {peti_kocka_2},
{peti_kocka_3}'#39;)
        robi_nyert +=1
        print(f'#39;A(z) {i+1}. körben Robi nyert!'#39;)
    else:
        print(f'#39;Robi dobásainak értéke: {robi_kocka_1}, {robi_kocka_2},
{robi_kocka_3}'#39;)
        print(f'#39;Peti dobásainak értéke: {peti_kocka_1}, {peti_kocka_2},
{peti_kocka_3}'#39;)
        peti_nyert +=1
        print(f'#39;A(z) {i+1}. körben Peti nyert!'#39;)
print(f'#39;Robi ennyi kört nyer: {robi_nyert}'#39;)
print(f'#39;Peti ennyi kört nyer: {peti_nyert}'#39;)
if robi_nyert'gt;peti_nyert:
    print('#39;Robi az abszolút győztes'#39;)
else:
     print('Peti az abszolút győztes')