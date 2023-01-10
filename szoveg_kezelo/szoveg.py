import os
import platform

def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    
torles()

teljes_nev = 'szabo ferenc'

#nagybetu
print(teljes_nev.upper())

elso_nagy = []
elso_betu = 0

for betu in teljes_nev:
    if betu == teljes_nev[0] and elso_betu == 0:
        elso_nagy.append(teljes_nev[0].upper())
        elso_betu += 1
    elif betu == ' ':
        elso_nagy.append(betu)
        elso_nagy.append(teljes_nev[teljes_nev.index(' ') + 1].upper())
        
    else:
        elso_nagy.append(betu)
    
elso_nagy.remove(teljes_nev[teljes_nev.index(' ') + 1])


print(*elso_nagy)


#karakterszamlalas

karakter = 0

for betu in teljes_nev:
    karakter += 1

print(f'A neved: {karakter} karakterbol all!')

#szokoz helye

szokoz = elso_nagy.index(' ') + 1
print(f'A nevedben a {szokoz} helyen all a szokoz')


#vezeteknev
print('A vezetekneved:')
print(*elso_nagy[0:szokoz - 1])
print('')

#keresztnev
print('A keresztneved:')
print(*elso_nagy[szokoz:len(elso_nagy)])
print('')


#vezeteknev hossza
print(f'A vezetekneved {szokoz - 1} hosszu')

#keresztnev hossza
print(f'A keresztneved {len(elso_nagy) - szokoz} hosszu')

#keresztnév helye
print(f'A keresztneved a {szokoz + 1}. helytol kezdodik')

#nevegyesites

a = 'Kiss'
b = 'Feri'

print(f'{a} {b}')


